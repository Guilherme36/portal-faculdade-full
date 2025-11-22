import pytest
import os
import uuid
os.environ['DATABASE_URL'] = f'sqlite:///:memory:'

from services import StudentService, TeacherService, SubjectService, ClassService
from database import init_db

@pytest.fixture(scope='function')
def setup_db():
    init_db()
    yield

def test_create_student(setup_db):
    uid = str(uuid.uuid4())[:8]
    student = StudentService.create(f"Aluno {uid}", f"aluno{uid}@test.com", f"M{uid}")
    assert student.id is not None
    assert student.nome == f"Aluno {uid}"

def test_list_students(setup_db):
    uid1 = str(uuid.uuid4())[:8]
    uid2 = str(uuid.uuid4())[:8]
    StudentService.create(f"Aluno {uid1}", f"a{uid1}@test.com", f"M{uid1}")
    StudentService.create(f"Aluno {uid2}", f"a{uid2}@test.com", f"M{uid2}")
    
    students = StudentService.list_all()
    assert len(students) >= 2

def test_update_student(setup_db):
    uid = str(uuid.uuid4())[:8]
    student = StudentService.create(f"Aluno {uid}", f"a{uid}@test.com", f"M{uid}")
    updated = StudentService.update(student.id, "Aluno Atualizado", f"a{uid}@test.com", f"M{uid}")
    
    assert updated.nome == "Aluno Atualizado"

def test_delete_student(setup_db):
    uid = str(uuid.uuid4())[:8]
    student = StudentService.create(f"Aluno {uid}", f"a{uid}@test.com", f"M{uid}")
    result = StudentService.delete(student.id)
    assert result is True
    
    retrieved = StudentService.get(student.id)
    assert retrieved is None

def test_create_teacher(setup_db):
    uid = str(uuid.uuid4())[:8]
    teacher = TeacherService.create(f"Prof {uid}", f"prof{uid}@test.com", "Computação")
    assert teacher.id is not None
    assert teacher.area == "Computação"

def test_create_subject(setup_db):
    subject = SubjectService.create("Programação Distribuída", "Sistemas distribuídos", 80)
    assert subject.id is not None
    assert subject.carga_horaria == 80

def test_create_class(setup_db):
    uid = str(uuid.uuid4())[:8]
    teacher = TeacherService.create(f"Prof {uid}", f"prof{uid}@test.com", "Computação")
    subject = SubjectService.create("Programação Distribuída", "Sistemas distribuídos", 80)
    
    cls = ClassService.create(subject.id, teacher.id, "Segunda", "19:00", "21:00")
    assert cls.id is not None
    assert cls.materia_id == subject.id

def test_enroll_student(setup_db):
    uid = str(uuid.uuid4())[:8]
    teacher = TeacherService.create(f"Prof {uid}", f"prof{uid}@test.com", "Computação")
    subject = SubjectService.create("Programação Distribuída", "Sistemas distribuídos", 80)
    cls = ClassService.create(subject.id, teacher.id, "Segunda", "19:00", "21:00")
    student = StudentService.create(f"Aluno {uid}", f"a{uid}@test.com", f"M{uid}")
    
    success, message = ClassService.enroll_student(cls.id, student.id)
    assert success is True
    assert "sucesso" in message.lower()
