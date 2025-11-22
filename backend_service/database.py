import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/turmas_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Tabela de associação para inscrições
enrollment_table = Table(
    'enrollments',
    Base.metadata,
    Column('class_id', Integer, ForeignKey('classes.id'), primary_key=True),
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    matricula = Column(String, unique=True, nullable=False)
    classes = relationship('Class', secondary=enrollment_table, back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    area = Column(String, nullable=False)
    classes = relationship('Class', back_populates='teacher', cascade='all, delete-orphan')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    carga_horaria = Column(Integer, nullable=False)
    classes = relationship('Class', back_populates='subject', cascade='all, delete-orphan')

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, index=True)
    materia_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    professor_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    dia_semana = Column(String, nullable=False)
    hora_inicio = Column(String, nullable=False)
    hora_fim = Column(String, nullable=False)
    
    subject = relationship('Subject', back_populates='classes')
    teacher = relationship('Teacher', back_populates='classes')
    students = relationship('Student', secondary=enrollment_table, back_populates='classes')

class EnrollmentEvent(Base):
    __tablename__ = 'enrollment_events'
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    timestamp = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)
