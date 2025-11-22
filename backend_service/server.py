import grpc
from concurrent import futures
import time
import sys
import os

# Adicionar diretório ao path para imports
sys.path.insert(0, os.path.dirname(__file__))

from protos import student_pb2, student_pb2_grpc
from protos import teacher_pb2, teacher_pb2_grpc
from protos import subject_pb2, subject_pb2_grpc
from protos import class_pb2, class_pb2_grpc
from services import StudentService, TeacherService, SubjectService, ClassService
from database import init_db

class StudentServicer(student_pb2_grpc.StudentServiceServicer):
    def CreateStudent(self, request, context):
        student = StudentService.create(request.nome, request.email, request.matricula)
        return student_pb2.StudentResponse(
            student=student_pb2.Student(
                id=student.id,
                nome=student.nome,
                email=student.email,
                matricula=student.matricula
            )
        )
    
    def GetStudent(self, request, context):
        student = StudentService.get(request.id)
        if not student:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Aluno não encontrado')
            return student_pb2.StudentResponse()
        
        return student_pb2.StudentResponse(
            student=student_pb2.Student(
                id=student.id,
                nome=student.nome,
                email=student.email,
                matricula=student.matricula
            )
        )
    
    def ListStudents(self, request, context):
        students = StudentService.list_all()
        return student_pb2.ListStudentsResponse(
            students=[
                student_pb2.Student(
                    id=s.id,
                    nome=s.nome,
                    email=s.email,
                    matricula=s.matricula
                ) for s in students
            ]
        )
    
    def UpdateStudent(self, request, context):
        student = StudentService.update(request.id, request.nome, request.email, request.matricula)
        if not student:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Aluno não encontrado')
            return student_pb2.StudentResponse()
        
        return student_pb2.StudentResponse(
            student=student_pb2.Student(
                id=student.id,
                nome=student.nome,
                email=student.email,
                matricula=student.matricula
            )
        )
    
    def DeleteStudent(self, request, context):
        success = StudentService.delete(request.id)
        return student_pb2.DeleteStudentResponse(success=success)

class TeacherServicer(teacher_pb2_grpc.TeacherServiceServicer):
    def CreateTeacher(self, request, context):
        teacher = TeacherService.create(request.nome, request.email, request.area)
        return teacher_pb2.TeacherResponse(
            teacher=teacher_pb2.Teacher(
                id=teacher.id,
                nome=teacher.nome,
                email=teacher.email,
                area=teacher.area
            )
        )
    
    def GetTeacher(self, request, context):
        teacher = TeacherService.get(request.id)
        if not teacher:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Professor não encontrado')
            return teacher_pb2.TeacherResponse()
        
        return teacher_pb2.TeacherResponse(
            teacher=teacher_pb2.Teacher(
                id=teacher.id,
                nome=teacher.nome,
                email=teacher.email,
                area=teacher.area
            )
        )
    
    def ListTeachers(self, request, context):
        teachers = TeacherService.list_all()
        return teacher_pb2.ListTeachersResponse(
            teachers=[
                teacher_pb2.Teacher(
                    id=t.id,
                    nome=t.nome,
                    email=t.email,
                    area=t.area
                ) for t in teachers
            ]
        )
    
    def UpdateTeacher(self, request, context):
        teacher = TeacherService.update(request.id, request.nome, request.email, request.area)
        if not teacher:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Professor não encontrado')
            return teacher_pb2.TeacherResponse()
        
        return teacher_pb2.TeacherResponse(
            teacher=teacher_pb2.Teacher(
                id=teacher.id,
                nome=teacher.nome,
                email=teacher.email,
                area=teacher.area
            )
        )
    
    def DeleteTeacher(self, request, context):
        success = TeacherService.delete(request.id)
        return teacher_pb2.DeleteTeacherResponse(success=success)

class SubjectServicer(subject_pb2_grpc.SubjectServiceServicer):
    def CreateSubject(self, request, context):
        subject = SubjectService.create(request.nome, request.descricao, request.carga_horaria)
        return subject_pb2.SubjectResponse(
            subject=subject_pb2.Subject(
                id=subject.id,
                nome=subject.nome,
                descricao=subject.descricao,
                carga_horaria=subject.carga_horaria
            )
        )
    
    def GetSubject(self, request, context):
        subject = SubjectService.get(request.id)
        if not subject:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Matéria não encontrada')
            return subject_pb2.SubjectResponse()
        
        return subject_pb2.SubjectResponse(
            subject=subject_pb2.Subject(
                id=subject.id,
                nome=subject.nome,
                descricao=subject.descricao,
                carga_horaria=subject.carga_horaria
            )
        )
    
    def ListSubjects(self, request, context):
        subjects = SubjectService.list_all()
        return subject_pb2.ListSubjectsResponse(
            subjects=[
                subject_pb2.Subject(
                    id=s.id,
                    nome=s.nome,
                    descricao=s.descricao,
                    carga_horaria=s.carga_horaria
                ) for s in subjects
            ]
        )
    
    def UpdateSubject(self, request, context):
        subject = SubjectService.update(request.id, request.nome, request.descricao, request.carga_horaria)
        if not subject:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Matéria não encontrada')
            return subject_pb2.SubjectResponse()
        
        return subject_pb2.SubjectResponse(
            subject=subject_pb2.Subject(
                id=subject.id,
                nome=subject.nome,
                descricao=subject.descricao,
                carga_horaria=subject.carga_horaria
            )
        )
    
    def DeleteSubject(self, request, context):
        success = SubjectService.delete(request.id)
        return subject_pb2.DeleteSubjectResponse(success=success)

class ClassServicer(class_pb2_grpc.ClassServiceServicer):
    def CreateClass(self, request, context):
        try:
            cls = ClassService.create(
                request.materia_id,
                request.professor_id,
                request.dia_semana,
                request.hora_inicio,
                request.hora_fim
            )
            return class_pb2.ClassResponse(
                turma=class_pb2.Class(
                    id=cls.id,
                    materia_id=cls.materia_id,
                    professor_id=cls.professor_id,
                    dia_semana=cls.dia_semana,
                    hora_inicio=cls.hora_inicio,
                    hora_fim=cls.hora_fim,
                    aluno_ids=[s.id for s in cls.students]
                )
            )
        except ValueError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            return class_pb2.ClassResponse()
    
    def GetClass(self, request, context):
        cls = ClassService.get(request.id)
        if not cls:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Turma não encontrada')
            return class_pb2.ClassResponse()
        
        return class_pb2.ClassResponse(
            turma=class_pb2.Class(
                id=cls.id,
                materia_id=cls.materia_id,
                professor_id=cls.professor_id,
                dia_semana=cls.dia_semana,
                hora_inicio=cls.hora_inicio,
                hora_fim=cls.hora_fim,
                aluno_ids=[s.id for s in cls.students]
            )
        )
    
    def ListClasses(self, request, context):
        classes = ClassService.list_all()
        return class_pb2.ListClassesResponse(
            classes=[
                class_pb2.Class(
                    id=c.id,
                    materia_id=c.materia_id,
                    professor_id=c.professor_id,
                    dia_semana=c.dia_semana,
                    hora_inicio=c.hora_inicio,
                    hora_fim=c.hora_fim,
                    aluno_ids=[s.id for s in c.students]
                ) for c in classes
            ]
        )
    
    def UpdateClass(self, request, context):
        cls = ClassService.update(
            request.id,
            request.materia_id,
            request.professor_id,
            request.dia_semana,
            request.hora_inicio,
            request.hora_fim
        )
        if not cls:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Turma não encontrada')
            return class_pb2.ClassResponse()
        
        return class_pb2.ClassResponse(
            turma=class_pb2.Class(
                id=cls.id,
                materia_id=cls.materia_id,
                professor_id=cls.professor_id,
                dia_semana=cls.dia_semana,
                hora_inicio=cls.hora_inicio,
                hora_fim=cls.hora_fim,
                aluno_ids=[s.id for s in cls.students]
            )
        )
    
    def DeleteClass(self, request, context):
        success = ClassService.delete(request.id)
        return class_pb2.DeleteClassResponse(success=success)
    
    def EnrollStudent(self, request, context):
        success, message = ClassService.enroll_student(request.class_id, request.student_id)
        return class_pb2.EnrollmentResponse(success=success, message=message)
    
    def GetClassStats(self, request, context):
        stats = ClassService.get_stats()
        return class_pb2.ClassStatsResponse(
            stats=[
                class_pb2.ClassStat(
                    class_id=s['class_id'],
                    student_count=s['student_count'],
                    professor_id=s['professor_id'],
                    materia_nome=s['materia_nome']
                ) for s in stats
            ]
        )

def serve():
    # Aguardar banco de dados estar pronto
    time.sleep(5)
    
    # Inicializar banco de dados
    init_db()
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    student_pb2_grpc.add_StudentServiceServicer_to_server(StudentServicer(), server)
    teacher_pb2_grpc.add_TeacherServiceServicer_to_server(TeacherServicer(), server)
    subject_pb2_grpc.add_SubjectServiceServicer_to_server(SubjectServicer(), server)
    class_pb2_grpc.add_ClassServiceServicer_to_server(ClassServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
