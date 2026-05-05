import pytest
from uctest.02_(python) import verificar_login, criar_conta, dados_usuario

@pytest.fixture(autouse=True)
def reset_usuarios():
    usuarios.clear()
    usuarios.update({"admin": "1234"})

def test_sql_injection_login():
    assert verificar_login("' OR '1'='1", "' OR '1'='1") == False

def test_script_injection():
    assert verificar_login("<script>alert(1)</script>", "1234") == False

def test_comando_malicioso():
    assert verificar_login("admin; DROP TABLE users", "1234") == False

def test_forca_bruta_simples():
    for _ in range(1000):
        assert verificar_login("admin", "senha_errada") == False

def test_usuario_muito_grande():
    usuario = "a" * 10000
    senha = "b" * 10000
    assert criar_conta(usuario, senha) == "sucesso"

def test_campos_none():
    assert verificar_login(None, None) == False
