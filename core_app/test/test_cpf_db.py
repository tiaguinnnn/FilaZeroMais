# tests/test_paciente_cpf.py
import pytest
from django.db import IntegrityError
from django.contrib.auth.models import User
from core_app.models import Paciente

@pytest.mark.django_db
def test_nao_deve_permitir_cadastro_de_cpf_duplicado():
    # Arrange: cria o 1º user e paciente
    user1 = User.objects.create_user(username="user1", password="pass")
    Paciente.objects.create(
        user=user1,
        nome="Paciente 1",
        cpf="12345678901",
        telefone="(67) 99999-0001",
        email="p1@example.com"
    )

    # Act & Assert: tenta criar 2º paciente (com outro user) com o MESMO CPF
    user2 = User.objects.create_user(username="user2", password="pass")
    with pytest.raises(IntegrityError):
        Paciente.objects.create(
            user=user2,
            nome="Paciente 2",
            cpf="12345678901",    # duplicado
            telefone="(67) 99999-0002",
            email="p2@example.com"
        )