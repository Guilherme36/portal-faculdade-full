from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Teacher(_message.Message):
    __slots__ = ("id", "nome", "email", "area")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    email: str
    area: str
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., area: _Optional[str] = ...) -> None: ...

class CreateTeacherRequest(_message.Message):
    __slots__ = ("nome", "email", "area")
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    nome: str
    email: str
    area: str
    def __init__(self, nome: _Optional[str] = ..., email: _Optional[str] = ..., area: _Optional[str] = ...) -> None: ...

class GetTeacherRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListTeachersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTeachersResponse(_message.Message):
    __slots__ = ("teachers",)
    TEACHERS_FIELD_NUMBER: _ClassVar[int]
    teachers: _containers.RepeatedCompositeFieldContainer[Teacher]
    def __init__(self, teachers: _Optional[_Iterable[_Union[Teacher, _Mapping]]] = ...) -> None: ...

class UpdateTeacherRequest(_message.Message):
    __slots__ = ("id", "nome", "email", "area")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    email: str
    area: str
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., area: _Optional[str] = ...) -> None: ...

class DeleteTeacherRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteTeacherResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class TeacherResponse(_message.Message):
    __slots__ = ("teacher",)
    TEACHER_FIELD_NUMBER: _ClassVar[int]
    teacher: Teacher
    def __init__(self, teacher: _Optional[_Union[Teacher, _Mapping]] = ...) -> None: ...
