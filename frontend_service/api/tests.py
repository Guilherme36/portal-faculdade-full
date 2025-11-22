from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch, MagicMock

class StudentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @patch('api.views.grpc_client')
    def test_create_student(self, mock_grpc):
        # Mock da resposta gRPC
        mock_response = MagicMock()
        mock_response.student.id = 1
        mock_response.student.nome = "João Silva"
        mock_response.student.email = "joao@email.com"
        mock_response.student.matricula = "2024001"
        mock_grpc.create_student.return_value = mock_response
        
        data = {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'matricula': '2024001'
        }
        
        response = self.client.post('/api/alunos/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'João Silva')
        self.assertEqual(response.data['email'], 'joao@email.com')
    
    @patch('api.views.grpc_client')
    def test_list_students(self, mock_grpc):
        # Mock da resposta gRPC
        mock_student1 = MagicMock()
        mock_student1.id = 1
        mock_student1.nome = "João Silva"
        mock_student1.email = "joao@email.com"
        mock_student1.matricula = "2024001"
        
        mock_student2 = MagicMock()
        mock_student2.id = 2
        mock_student2.nome = "Maria Santos"
        mock_student2.email = "maria@email.com"
        mock_student2.matricula = "2024002"
        
        mock_response = MagicMock()
        mock_response.students = [mock_student1, mock_student2]
        mock_grpc.list_students.return_value = mock_response
        
        response = self.client.get('/api/alunos/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class TeacherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @patch('api.views.grpc_client')
    def test_create_teacher(self, mock_grpc):
        mock_response = MagicMock()
        mock_response.teacher.id = 1
        mock_response.teacher.nome = "Prof. Maria"
        mock_response.teacher.email = "maria@email.com"
        mock_response.teacher.area = "Computação"
        mock_grpc.create_teacher.return_value = mock_response
        
        data = {
            'nome': 'Prof. Maria',
            'email': 'maria@email.com',
            'area': 'Computação'
        }
        
        response = self.client.post('/api/professores/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Prof. Maria')

class ClassAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @patch('api.views.grpc_client')
    def test_enroll_student(self, mock_grpc):
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.message = "Inscrição realizada com sucesso"
        mock_grpc.enroll_student.return_value = mock_response
        
        data = {'aluno_id': 1}
        
        response = self.client.post('/api/turmas/1/inscricoes/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
