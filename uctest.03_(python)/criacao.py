import pytest
import uctest.02_(python) import verificaar_login, criar_conta, usuarios

@pytest.fixture(autouse=True)
def reset_usuarios():
    usuarios.clear()
    usuarios.update({"admin": "1234"})

def test_criar_conta_sucesso():
    resultado = criar_conta("novo", "123")
    assert resultado == "sucesso"
    assert usuarios["novo"] == "123"

def test_criar_usuario_existente():
    resultado = criar_conta("admin", "1234")
    assert resultado == "usuario_existente"

def test_criar_conta_usuario_vazio():
    assert criar_conta("", "123") == "campos_vazios"
    
def test_criar_conta_senha_vazia():
    assert criar_conta("user", "") == "campos_vazios"

def test_criar_conta_ambos_vazios():
    assert criar_conta("", "") == "campos_vazios"
    