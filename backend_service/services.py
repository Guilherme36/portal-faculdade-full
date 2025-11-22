from database import Student, Teacher, Subject, Class, SessionLocal
from message_queue import publish_enrollment

class StudentService:
    @staticmethod
    def create(nome, email, matricula):
        db = SessionLocal()
        try:
            student = Student(nome=nome, email=email, matricula=matricula)
            db.add(student)
            db.commit()
            db.refresh(student)
            return student
        finally:
            db.close()
    
    @staticmethod
    def get(student_id):
        db = SessionLocal()
        try:
            return db.query(Student).filter(Student.id == student_id).first()
        finally:
            db.close()
    
    @staticmethod
    def list_all():
        db = SessionLocal()
        try:
            return db.query(Student).all()
        finally:
            db.close()
    
    @staticmethod
    def update(student_id, nome, email, matricula):
        db = SessionLocal()
        try:
            student = db.query(Student).filter(Student.id == student_id).first()
            if student:
                student.nome = nome
                student.email = email
                student.matricula = matricula
                db.commit()
                db.refresh(student)
            return student
        finally:
            db.close()
    
    @staticmethod
    def delete(student_id):
        db = SessionLocal()
        try:
            student = db.query(Student).filter(Student.id == student_id).first()
            if student:
                db.delete(student)
                db.commit()
                return True
            return False
        finally:
            db.close()

class TeacherService:
    @staticmethod
    def create(nome, email, area):
        db = SessionLocal()
        try:
            teacher = Teacher(nome=nome, email=email, area=area)
            db.add(teacher)
            db.commit()
            db.refresh(teacher)
            return teacher
        finally:
            db.close()
    
    @staticmethod
    def get(teacher_id):
        db = SessionLocal()
        try:
            return db.query(Teacher).filter(Teacher.id == teacher_id).first()
        finally:
            db.close()
    
    @staticmethod
    def list_all():
        db = SessionLocal()
        try:
            return db.query(Teacher).all()
        finally:
            db.close()
    
    @staticmethod
    def update(teacher_id, nome, email, area):
        db = SessionLocal()
        try:
            teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
            if teacher:
                teacher.nome = nome
                teacher.email = email
                teacher.area = area
                db.commit()
                db.refresh(teacher)
            return teacher
        finally:
            db.close()
    
    @staticmethod
    def delete(teacher_id):
        db = SessionLocal()
        try:
            teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
            if teacher:
                db.delete(teacher)
                db.commit()
                return True
            return False
        finally:
            db.close()

class SubjectService:
    @staticmethod
    def create(nome, descricao, carga_horaria):
        db = SessionLocal()
        try:
            subject = Subject(nome=nome, descricao=descricao, carga_horaria=carga_horaria)
            db.add(subject)
            db.commit()
            db.refresh(subject)
            return subject
        finally:
            db.close()
    
    @staticmethod
    def get(subject_id):
        db = SessionLocal()
        try:
            return db.query(Subject).filter(Subject.id == subject_id).first()
        finally:
            db.close()
    
    @staticmethod
    def list_all():
        db = SessionLocal()
        try:
            return db.query(Subject).all()
        finally:
            db.close()
    
    @staticmethod
    def update(subject_id, nome, descricao, carga_horaria):
        db = SessionLocal()
        try:
            subject = db.query(Subject).filter(Subject.id == subject_id).first()
            if subject:
                subject.nome = nome
                subject.descricao = descricao
                subject.carga_horaria = carga_horaria
                db.commit()
                db.refresh(subject)
            return subject
        finally:
            db.close()
    
    @staticmethod
    def delete(subject_id):
        db = SessionLocal()
        try:
            subject = db.query(Subject).filter(Subject.id == subject_id).first()
            if subject:
                db.delete(subject)
                db.commit()
                return True
            return False
        finally:
            db.close()

class ClassService:
    @staticmethod
    def create(materia_id, professor_id, dia_semana, hora_inicio, hora_fim):
        db = SessionLocal()
        try:
            conflicts = db.query(Class).filter(
                Class.professor_id == professor_id,
                Class.dia_semana == dia_semana
            ).all()
            
            for c in conflicts:
                if not (hora_fim <= c.hora_inicio or hora_inicio >= c.hora_fim):
                    raise ValueError("Conflito de horário para o professor")
            
            cls = Class(
                materia_id=materia_id,
                professor_id=professor_id,
                dia_semana=dia_semana,
                hora_inicio=hora_inicio,
                hora_fim=hora_fim
            )
            db.add(cls)
            db.commit()
            db.refresh(cls)
            _ = cls.students
            _ = cls.subject
            return cls
        finally:
            db.close()
    
    @staticmethod
    def get(class_id):
        db = SessionLocal()
        try:
            cls = db.query(Class).filter(Class.id == class_id).first()
            if cls:
                # Forçar carregamento dos relacionamentos
                _ = cls.students
                _ = cls.subject
            return cls
        finally:
            db.close()
    
    @staticmethod
    def list_all():
        db = SessionLocal()
        try:
            classes = db.query(Class).all()
            # Forçar carregamento dos relacionamentos
            for cls in classes:
                _ = cls.students
                _ = cls.subject
            return classes
        finally:
            db.close()
    
    @staticmethod
    def update(class_id, materia_id, professor_id, dia_semana, hora_inicio, hora_fim):
        db = SessionLocal()
        try:
            cls = db.query(Class).filter(Class.id == class_id).first()
            if cls:
                cls.materia_id = materia_id
                cls.professor_id = professor_id
                cls.dia_semana = dia_semana
                cls.hora_inicio = hora_inicio
                cls.hora_fim = hora_fim
                db.commit()
                db.refresh(cls)
            return cls
        finally:
            db.close()
    
    @staticmethod
    def delete(class_id):
        db = SessionLocal()
        try:
            cls = db.query(Class).filter(Class.id == class_id).first()
            if cls:
                db.delete(cls)
                db.commit()
                return True
            return False
        finally:
            db.close()
    
    @staticmethod
    def enroll_student(class_id, student_id):
        db = SessionLocal()
        try:
            cls = db.query(Class).filter(Class.id == class_id).first()
            student = db.query(Student).filter(Student.id == student_id).first()
            
            if not cls or not student:
                return False, "Turma ou aluno não encontrado"
            
            if student in cls.students:
                return False, "Aluno já inscrito nesta turma"
            
            cls.students.append(student)
            db.commit()
            
            # Publicar mensagem no RabbitMQ
            publish_enrollment(class_id, student_id)
            
            return True, "Inscrição realizada com sucesso"
        finally:
            db.close()
    
    @staticmethod
    def get_stats():
        db = SessionLocal()
        try:
            classes = db.query(Class).all()
            stats = []
            for cls in classes:
                stats.append({
                    'class_id': cls.id,
                    'student_count': len(cls.students),
                    'professor_id': cls.professor_id,
                    'materia_nome': cls.subject.nome if cls.subject else ''
                })
            return stats
        finally:
            db.close()
