
def criar_conta(usuario, senha):
    if not isinstance(usuario, str) or not isinstance(senha, str):
        return "Campos_Invalidos"
    
    if not usuario or not senha:
        return "Campos_Vazios"
    
    if len(usuario) > 100 or len(senha > 100):
        return "Muito_grande"
    
    if usuario in usuarios:
        return "usuario_existe"
    
    usuarios[usuario] = senha
    return "Sucesso"
