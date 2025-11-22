from django.urls import path
from .views import (
    StudentListCreateView, StudentDetailView,
    TeacherListCreateView, TeacherDetailView,
    SubjectListCreateView, SubjectDetailView,
    ClassListCreateView, ClassDetailView,
    ClassEnrollmentView, ClassReportView
)
from . import web_views

urlpatterns = [
    # API REST
    path('api/alunos/', StudentListCreateView.as_view()),
    path('api/alunos/<int:pk>/', StudentDetailView.as_view()),
    path('api/professores/', TeacherListCreateView.as_view()),
    path('api/professores/<int:pk>/', TeacherDetailView.as_view()),
    path('api/materias/', SubjectListCreateView.as_view()),
    path('api/materias/<int:pk>/', SubjectDetailView.as_view()),
    path('api/turmas/', ClassListCreateView.as_view()),
    path('api/turmas/<int:pk>/', ClassDetailView.as_view()),
    path('api/turmas/<int:pk>/inscricoes/', ClassEnrollmentView.as_view()),
    path('api/relatorios/turmas/', ClassReportView.as_view()),
    
    # Páginas HTML
    path('', web_views.index),
    path('alunos', web_views.alunos),
    path('professores', web_views.professores),
    path('materias', web_views.materias),
    path('turmas', web_views.turmas),
]
