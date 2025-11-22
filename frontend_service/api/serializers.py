from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    matricula = serializers.CharField(max_length=50)

class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    area = serializers.CharField(max_length=100)

class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=200)
    descricao = serializers.CharField(required=False, allow_blank=True)
    carga_horaria = serializers.IntegerField()

class ClassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    materia_id = serializers.IntegerField()
    professor_id = serializers.IntegerField()
    dia_semana = serializers.CharField(max_length=20)
    hora_inicio = serializers.CharField(max_length=10)
    hora_fim = serializers.CharField(max_length=10)
    aluno_ids = serializers.ListField(
        child=serializers.IntegerField(),
        read_only=True
    )

class EnrollmentSerializer(serializers.Serializer):
    aluno_id = serializers.IntegerField()
