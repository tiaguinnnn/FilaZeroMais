import pytest

@pytest.mark.django_db
def test_garantir_presenca_de_protecao_csrf_na_home(client):
    # ARRANGE
    url_cadastro = '/register/'

    # ACT
    response = client.get(url_cadastro)

    # ASSERT
    # Verifica se o token de segurança CSRF está presente no HTML da página
    assert 'csrfmiddlewaretoken' in response.content.decode('utf-8'), \
        "ALERTA DE SEGURANÇA: O formulário está desprotegido contra ataques CSRF!"