from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ("id", "nome", "email", "matricula")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    email: str
    matricula: str
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., matricula: _Optional[str] = ...) -> None: ...

class CreateStudentRequest(_message.Message):
    __slots__ = ("nome", "email", "matricula")
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    nome: str
    email: str
    matricula: str
    def __init__(self, nome: _Optional[str] = ..., email: _Optional[str] = ..., matricula: _Optional[str] = ...) -> None: ...

class GetStudentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListStudentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListStudentsResponse(_message.Message):
    __slots__ = ("students",)
    STUDENTS_FIELD_NUMBER: _ClassVar[int]
    students: _containers.RepeatedCompositeFieldContainer[Student]
    def __init__(self, students: _Optional[_Iterable[_Union[Student, _Mapping]]] = ...) -> None: ...

class UpdateStudentRequest(_message.Message):
    __slots__ = ("id", "nome", "email", "matricula")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    email: str
    matricula: str
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., matricula: _Optional[str] = ...) -> None: ...

class DeleteStudentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteStudentResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class StudentResponse(_message.Message):
    __slots__ = ("student",)
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: Student
    def __init__(self, student: _Optional[_Union[Student, _Mapping]] = ...) -> None: ...
