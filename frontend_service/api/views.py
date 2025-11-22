import grpc
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .grpc_client import grpc_client
from .serializers import (
    StudentSerializer, TeacherSerializer, 
    SubjectSerializer, ClassSerializer, EnrollmentSerializer
)

class StudentListCreateView(APIView):
    def get(self, request):
        try:
            response = grpc_client.list_students()
            students = [
                {
                    'id': s.id,
                    'nome': s.nome,
                    'email': s.email,
                    'matricula': s.matricula
                }
                for s in response.students
            ]
            return Response(students)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.create_student(
                    serializer.validated_data['nome'],
                    serializer.validated_data['email'],
                    serializer.validated_data['matricula']
                )
                return Response({
                    'id': response.student.id,
                    'nome': response.student.nome,
                    'email': response.student.email,
                    'matricula': response.student.matricula
                }, status=status.HTTP_201_CREATED)
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, pk):
        try:
            response = grpc_client.get_student(pk)
            return Response({
                'id': response.student.id,
                'nome': response.student.nome,
                'email': response.student.email,
                'matricula': response.student.matricula
            })
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def put(self, request, pk):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.update_student(
                    pk,
                    serializer.validated_data['nome'],
                    serializer.validated_data['email'],
                    serializer.validated_data['matricula']
                )
                return Response({
                    'id': response.student.id,
                    'nome': response.student.nome,
                    'email': response.student.email,
                    'matricula': response.student.matricula
                })
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            grpc_client.delete_student(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )

class TeacherListCreateView(APIView):
    def get(self, request):
        try:
            response = grpc_client.list_teachers()
            teachers = [
                {
                    'id': t.id,
                    'nome': t.nome,
                    'email': t.email,
                    'area': t.area
                }
                for t in response.teachers
            ]
            return Response(teachers)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.create_teacher(
                    serializer.validated_data['nome'],
                    serializer.validated_data['email'],
                    serializer.validated_data['area']
                )
                return Response({
                    'id': response.teacher.id,
                    'nome': response.teacher.nome,
                    'email': response.teacher.email,
                    'area': response.teacher.area
                }, status=status.HTTP_201_CREATED)
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, pk):
        try:
            response = grpc_client.get_teacher(pk)
            return Response({
                'id': response.teacher.id,
                'nome': response.teacher.nome,
                'email': response.teacher.email,
                'area': response.teacher.area
            })
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def put(self, request, pk):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.update_teacher(
                    pk,
                    serializer.validated_data['nome'],
                    serializer.validated_data['email'],
                    serializer.validated_data['area']
                )
                return Response({
                    'id': response.teacher.id,
                    'nome': response.teacher.nome,
                    'email': response.teacher.email,
                    'area': response.teacher.area
                })
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            grpc_client.delete_teacher(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )

class SubjectListCreateView(APIView):
    def get(self, request):
        try:
            response = grpc_client.list_subjects()
            subjects = [
                {
                    'id': s.id,
                    'nome': s.nome,
                    'descricao': s.descricao,
                    'carga_horaria': s.carga_horaria
                }
                for s in response.subjects
            ]
            return Response(subjects)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.create_subject(
                    serializer.validated_data['nome'],
                    serializer.validated_data.get('descricao', ''),
                    serializer.validated_data['carga_horaria']
                )
                return Response({
                    'id': response.subject.id,
                    'nome': response.subject.nome,
                    'descricao': response.subject.descricao,
                    'carga_horaria': response.subject.carga_horaria
                }, status=status.HTTP_201_CREATED)
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailView(APIView):
    def get(self, request, pk):
        try:
            response = grpc_client.get_subject(pk)
            return Response({
                'id': response.subject.id,
                'nome': response.subject.nome,
                'descricao': response.subject.descricao,
                'carga_horaria': response.subject.carga_horaria
            })
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def put(self, request, pk):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.update_subject(
                    pk,
                    serializer.validated_data['nome'],
                    serializer.validated_data.get('descricao', ''),
                    serializer.validated_data['carga_horaria']
                )
                return Response({
                    'id': response.subject.id,
                    'nome': response.subject.nome,
                    'descricao': response.subject.descricao,
                    'carga_horaria': response.subject.carga_horaria
                })
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            grpc_client.delete_subject(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )

class ClassListCreateView(APIView):
    def get(self, request):
        try:
            response = grpc_client.list_classes()
            classes = [
                {
                    'id': c.id,
                    'materia_id': c.materia_id,
                    'professor_id': c.professor_id,
                    'dia_semana': c.dia_semana,
                    'hora_inicio': c.hora_inicio,
                    'hora_fim': c.hora_fim,
                    'aluno_ids': list(c.aluno_ids)
                }
                for c in response.classes
            ]
            return Response(classes)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.create_class(
                    serializer.validated_data['materia_id'],
                    serializer.validated_data['professor_id'],
                    serializer.validated_data['dia_semana'],
                    serializer.validated_data['hora_inicio'],
                    serializer.validated_data['hora_fim']
                )
                return Response({
                    'id': response.turma.id,
                    'materia_id': response.turma.materia_id,
                    'professor_id': response.turma.professor_id,
                    'dia_semana': response.turma.dia_semana,
                    'hora_inicio': response.turma.hora_inicio,
                    'hora_fim': response.turma.hora_fim,
                    'aluno_ids': list(response.turma.aluno_ids)
                }, status=status.HTTP_201_CREATED)
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassDetailView(APIView):
    def get(self, request, pk):
        try:
            response = grpc_client.get_class(pk)
            return Response({
                'id': response.turma.id,
                'materia_id': response.turma.materia_id,
                'professor_id': response.turma.professor_id,
                'dia_semana': response.turma.dia_semana,
                'hora_inicio': response.turma.hora_inicio,
                'hora_fim': response.turma.hora_fim,
                'aluno_ids': list(response.turma.aluno_ids)
            })
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def put(self, request, pk):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.update_class(
                    pk,
                    serializer.validated_data['materia_id'],
                    serializer.validated_data['professor_id'],
                    serializer.validated_data['dia_semana'],
                    serializer.validated_data['hora_inicio'],
                    serializer.validated_data['hora_fim']
                )
                return Response({
                    'id': response.turma.id,
                    'materia_id': response.turma.materia_id,
                    'professor_id': response.turma.professor_id,
                    'dia_semana': response.turma.dia_semana,
                    'hora_inicio': response.turma.hora_inicio,
                    'hora_fim': response.turma.hora_fim,
                    'aluno_ids': list(response.turma.aluno_ids)
                })
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            grpc_client.delete_class(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_404_NOT_FOUND
            )

class ClassEnrollmentView(APIView):
    def post(self, request, pk):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response = grpc_client.enroll_student(
                    pk,
                    serializer.validated_data['aluno_id']
                )
                return Response({
                    'success': response.success,
                    'message': response.message
                }, status=status.HTTP_200_OK if response.success else status.HTTP_400_BAD_REQUEST)
            except grpc.RpcError as e:
                return Response(
                    {'error': str(e.details())},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassReportView(APIView):
    """
    Endpoint com processamento vetorizado usando pandas/numpy
    """
    def get(self, request):
        try:
            # Buscar dados via gRPC
            stats_response = grpc_client.get_class_stats()
            
            # Converter para DataFrame pandas para processamento vetorizado
            data = []
            for stat in stats_response.stats:
                data.append({
                    'class_id': stat.class_id,
                    'student_count': stat.student_count,
                    'professor_id': stat.professor_id,
                    'materia_nome': stat.materia_nome
                })
            
            if not data:
                return Response({
                    'total_turmas': 0,
                    'total_alunos': 0,
                    'media_alunos_por_turma': 0,
                    'turmas_por_professor': {},
                    'turmas': []
                })
            
            df = pd.DataFrame(data)
            
            # Processamento vetorizado com pandas/numpy
            total_turmas = len(df)
            total_alunos = np.sum(df['student_count'].values)
            media_alunos = np.mean(df['student_count'].values)
            
            # Agrupar turmas por professor
            turmas_por_professor = df.groupby('professor_id').size().to_dict()
            
            # Estatísticas por turma
            turmas_stats = df.to_dict('records')
            
            return Response({
                'total_turmas': int(total_turmas),
                'total_alunos': int(total_alunos),
                'media_alunos_por_turma': float(media_alunos),
                'turmas_por_professor': {int(k): int(v) for k, v in turmas_por_professor.items()},
                'turmas': turmas_stats
            })
        except grpc.RpcError as e:
            return Response(
                {'error': str(e.details())},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
