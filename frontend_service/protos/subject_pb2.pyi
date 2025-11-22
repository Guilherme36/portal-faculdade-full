from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subject(_message.Message):
    __slots__ = ("id", "nome", "descricao", "carga_horaria")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    CARGA_HORARIA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    descricao: str
    carga_horaria: int
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., carga_horaria: _Optional[int] = ...) -> None: ...

class CreateSubjectRequest(_message.Message):
    __slots__ = ("nome", "descricao", "carga_horaria")
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    CARGA_HORARIA_FIELD_NUMBER: _ClassVar[int]
    nome: str
    descricao: str
    carga_horaria: int
    def __init__(self, nome: _Optional[str] = ..., descricao: _Optional[str] = ..., carga_horaria: _Optional[int] = ...) -> None: ...

class GetSubjectRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListSubjectsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSubjectsResponse(_message.Message):
    __slots__ = ("subjects",)
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    subjects: _containers.RepeatedCompositeFieldContainer[Subject]
    def __init__(self, subjects: _Optional[_Iterable[_Union[Subject, _Mapping]]] = ...) -> None: ...

class UpdateSubjectRequest(_message.Message):
    __slots__ = ("id", "nome", "descricao", "carga_horaria")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    CARGA_HORARIA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    descricao: str
    carga_horaria: int
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., carga_horaria: _Optional[int] = ...) -> None: ...

class DeleteSubjectRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteSubjectResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class SubjectResponse(_message.Message):
    __slots__ = ("subject",)
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    subject: Subject
    def __init__(self, subject: _Optional[_Union[Subject, _Mapping]] = ...) -> None: ...
