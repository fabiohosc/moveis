### Dados "fixos" (simulando um banco de dados simples)
usuario_correto = "admin"
senha_correta = "1234"

### Entrada do usuário
usuario = input("Digite o usuário:\t") 
senha =  input("Digite a senha:\t")

### Verificação
if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso.")
else:
    print("Usuário oui senha incorretos.")
