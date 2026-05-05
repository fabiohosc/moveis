
usuarios = {
    "admin" : "1234"
}
tentativas = {}

def verificar_login(usuario, senha):
### Validação de Tipo
    if not isinstance(usuario, str) or not isinstance(senha, str):
        return False
    
### Limite de Tamanho
    if len(usuario) > 100 or len(senha > 100):
        return False
    
### Controle de Tentativas
    if usuario not in tentativas:
        tentativas[usuario] = 0

    if tentativas[usuario] >= 5:
        return "Bloqueado."
    
    if usuario in usuarios and usuarios[usuario] == senha:
        tentativas[usuario] = 0
        return True
    else:
        tentativas[usuario] = 0
        return False
