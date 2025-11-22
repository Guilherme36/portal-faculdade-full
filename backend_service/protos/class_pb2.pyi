from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Class(_message.Message):
    __slots__ = ("id", "materia_id", "professor_id", "dia_semana", "hora_inicio", "hora_fim", "aluno_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    MATERIA_ID_FIELD_NUMBER: _ClassVar[int]
    PROFESSOR_ID_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_FIELD_NUMBER: _ClassVar[int]
    HORA_INICIO_FIELD_NUMBER: _ClassVar[int]
    HORA_FIM_FIELD_NUMBER: _ClassVar[int]
    ALUNO_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    materia_id: int
    professor_id: int
    dia_semana: str
    hora_inicio: str
    hora_fim: str
    aluno_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., materia_id: _Optional[int] = ..., professor_id: _Optional[int] = ..., dia_semana: _Optional[str] = ..., hora_inicio: _Optional[str] = ..., hora_fim: _Optional[str] = ..., aluno_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateClassRequest(_message.Message):
    __slots__ = ("materia_id", "professor_id", "dia_semana", "hora_inicio", "hora_fim")
    MATERIA_ID_FIELD_NUMBER: _ClassVar[int]
    PROFESSOR_ID_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_FIELD_NUMBER: _ClassVar[int]
    HORA_INICIO_FIELD_NUMBER: _ClassVar[int]
    HORA_FIM_FIELD_NUMBER: _ClassVar[int]
    materia_id: int
    professor_id: int
    dia_semana: str
    hora_inicio: str
    hora_fim: str
    def __init__(self, materia_id: _Optional[int] = ..., professor_id: _Optional[int] = ..., dia_semana: _Optional[str] = ..., hora_inicio: _Optional[str] = ..., hora_fim: _Optional[str] = ...) -> None: ...

class GetClassRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListClassesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClassesResponse(_message.Message):
    __slots__ = ("classes",)
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[Class]
    def __init__(self, classes: _Optional[_Iterable[_Union[Class, _Mapping]]] = ...) -> None: ...

class UpdateClassRequest(_message.Message):
    __slots__ = ("id", "materia_id", "professor_id", "dia_semana", "hora_inicio", "hora_fim")
    ID_FIELD_NUMBER: _ClassVar[int]
    MATERIA_ID_FIELD_NUMBER: _ClassVar[int]
    PROFESSOR_ID_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_FIELD_NUMBER: _ClassVar[int]
    HORA_INICIO_FIELD_NUMBER: _ClassVar[int]
    HORA_FIM_FIELD_NUMBER: _ClassVar[int]
    id: int
    materia_id: int
    professor_id: int
    dia_semana: str
    hora_inicio: str
    hora_fim: str
    def __init__(self, id: _Optional[int] = ..., materia_id: _Optional[int] = ..., professor_id: _Optional[int] = ..., dia_semana: _Optional[str] = ..., hora_inicio: _Optional[str] = ..., hora_fim: _Optional[str] = ...) -> None: ...

class DeleteClassRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteClassResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ClassResponse(_message.Message):
    __slots__ = ("turma",)
    TURMA_FIELD_NUMBER: _ClassVar[int]
    turma: Class
    def __init__(self, turma: _Optional[_Union[Class, _Mapping]] = ...) -> None: ...

class EnrollStudentRequest(_message.Message):
    __slots__ = ("class_id", "student_id")
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: int
    student_id: int
    def __init__(self, class_id: _Optional[int] = ..., student_id: _Optional[int] = ...) -> None: ...

class EnrollmentResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetClassStatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClassStatsResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[ClassStat]
    def __init__(self, stats: _Optional[_Iterable[_Union[ClassStat, _Mapping]]] = ...) -> None: ...

class ClassStat(_message.Message):
    __slots__ = ("class_id", "student_count", "professor_id", "materia_nome")
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    STUDENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROFESSOR_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIA_NOME_FIELD_NUMBER: _ClassVar[int]
    class_id: int
    student_count: int
    professor_id: int
    materia_nome: str
    def __init__(self, class_id: _Optional[int] = ..., student_count: _Optional[int] = ..., professor_id: _Optional[int] = ..., materia_nome: _Optional[str] = ...) -> None: ...
