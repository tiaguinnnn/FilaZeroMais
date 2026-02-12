import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_deve_registrar_novo_usuario_com_sucesso_no_banco():
    """
    Testa se a persistência de dados do usuário respeita a integridade do banco.
    """
    # --- ARRANGE (Organizar) ---
    username_teste = "tiago_devops"
    email_teste = "tiago@hackathon.com"
    senha_teste = "senhaseguraConfia"

    # --- ACT (Agir) ---
    usuario_criado = User.objects.create_user(
        username=username_teste, 
        email=email_teste, 
        password=senha_teste
    )

    # --- ASSERT (Afirmar/Verificar) ---
    assert User.objects.count() == 1, "Erro: O usuário não foi salvo no banco de dados."
    assert usuario_criado.username == username_teste, f"Erro: Nome esperado {username_teste}, mas salvou {usuario_criado.username}"
    assert usuario_criado.email == email_teste, "Erro: O e-mail salvo está incorreto."