import pytest
from uctest.02_(python) import verificar_login, criar_conta, dados_usuario

@pytest.fixture9(autouse=True)
def reset_usuarios():
    usuarios.clear()
    usuarios.update({"admin": "1234"})

def test_login_valido():
    assert verificar_login("admin", "1234") == True

def test_login_usuario_inexistente():
    assert verificar_login("joao", "1234") == False

def test_login_senha_errada():
    assert verificar_login("admin", "0000") == False

def test_login_campos_vazios():
    assert verificar_login("", "") == False
