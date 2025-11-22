import grpc
import sys
import os
from django.conf import settings

# Adicionar diretório protos ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'protos'))

try:
    from protos import student_pb2, student_pb2_grpc
    from protos import teacher_pb2, teacher_pb2_grpc
    from protos import subject_pb2, subject_pb2_grpc
    from protos import class_pb2, class_pb2_grpc
except ImportError:
    # Fallback para desenvolvimento local
    import student_pb2, student_pb2_grpc
    import teacher_pb2, teacher_pb2_grpc
    import subject_pb2, subject_pb2_grpc
    import class_pb2, class_pb2_grpc

class GrpcClient:
    def __init__(self):
        self.channel = grpc.insecure_channel(settings.GRPC_HOST)
        self.student_stub = student_pb2_grpc.StudentServiceStub(self.channel)
        self.teacher_stub = teacher_pb2_grpc.TeacherServiceStub(self.channel)
        self.subject_stub = subject_pb2_grpc.SubjectServiceStub(self.channel)
        self.class_stub = class_pb2_grpc.ClassServiceStub(self.channel)
    
    # Student methods
    def create_student(self, nome, email, matricula):
        request = student_pb2.CreateStudentRequest(
            nome=nome, email=email, matricula=matricula
        )
        return self.student_stub.CreateStudent(request)
    
    def get_student(self, student_id):
        request = student_pb2.GetStudentRequest(id=student_id)
        return self.student_stub.GetStudent(request)
    
    def list_students(self):
        request = student_pb2.ListStudentsRequest()
        return self.student_stub.ListStudents(request)
    
    def update_student(self, student_id, nome, email, matricula):
        request = student_pb2.UpdateStudentRequest(
            id=student_id, nome=nome, email=email, matricula=matricula
        )
        return self.student_stub.UpdateStudent(request)
    
    def delete_student(self, student_id):
        request = student_pb2.DeleteStudentRequest(id=student_id)
        return self.student_stub.DeleteStudent(request)
    
    # Teacher methods
    def create_teacher(self, nome, email, area):
        request = teacher_pb2.CreateTeacherRequest(
            nome=nome, email=email, area=area
        )
        return self.teacher_stub.CreateTeacher(request)
    
    def get_teacher(self, teacher_id):
        request = teacher_pb2.GetTeacherRequest(id=teacher_id)
        return self.teacher_stub.GetTeacher(request)
    
    def list_teachers(self):
        request = teacher_pb2.ListTeachersRequest()
        return self.teacher_stub.ListTeachers(request)
    
    def update_teacher(self, teacher_id, nome, email, area):
        request = teacher_pb2.UpdateTeacherRequest(
            id=teacher_id, nome=nome, email=email, area=area
        )
        return self.teacher_stub.UpdateTeacher(request)
    
    def delete_teacher(self, teacher_id):
        request = teacher_pb2.DeleteTeacherRequest(id=teacher_id)
        return self.teacher_stub.DeleteTeacher(request)
    
    # Subject methods
    def create_subject(self, nome, descricao, carga_horaria):
        request = subject_pb2.CreateSubjectRequest(
            nome=nome, descricao=descricao, carga_horaria=carga_horaria
        )
        return self.subject_stub.CreateSubject(request)
    
    def get_subject(self, subject_id):
        request = subject_pb2.GetSubjectRequest(id=subject_id)
        return self.subject_stub.GetSubject(request)
    
    def list_subjects(self):
        request = subject_pb2.ListSubjectsRequest()
        return self.subject_stub.ListSubjects(request)
    
    def update_subject(self, subject_id, nome, descricao, carga_horaria):
        request = subject_pb2.UpdateSubjectRequest(
            id=subject_id, nome=nome, descricao=descricao, carga_horaria=carga_horaria
        )
        return self.subject_stub.UpdateSubject(request)
    
    def delete_subject(self, subject_id):
        request = subject_pb2.DeleteSubjectRequest(id=subject_id)
        return self.subject_stub.DeleteSubject(request)
    
    # Class methods
    def create_class(self, materia_id, professor_id, dia_semana, hora_inicio, hora_fim):
        request = class_pb2.CreateClassRequest(
            materia_id=materia_id,
            professor_id=professor_id,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim
        )
        return self.class_stub.CreateClass(request)
    
    def get_class(self, class_id):
        request = class_pb2.GetClassRequest(id=class_id)
        return self.class_stub.GetClass(request)
    
    def list_classes(self):
        request = class_pb2.ListClassesRequest()
        return self.class_stub.ListClasses(request)
    
    def update_class(self, class_id, materia_id, professor_id, dia_semana, hora_inicio, hora_fim):
        request = class_pb2.UpdateClassRequest(
            id=class_id,
            materia_id=materia_id,
            professor_id=professor_id,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim
        )
        return self.class_stub.UpdateClass(request)
    
    def delete_class(self, class_id):
        request = class_pb2.DeleteClassRequest(id=class_id)
        return self.class_stub.DeleteClass(request)
    
    def enroll_student(self, class_id, student_id):
        request = class_pb2.EnrollStudentRequest(
            class_id=class_id, student_id=student_id
        )
        return self.class_stub.EnrollStudent(request)
    
    def get_class_stats(self):
        request = class_pb2.GetClassStatsRequest()
        return self.class_stub.GetClassStats(request)

grpc_client = GrpcClient()
