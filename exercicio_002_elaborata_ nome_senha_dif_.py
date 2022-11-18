usuario = input("informe seu usuário: " )
senha = input("informe sua senha: ")

while usuario == senha:
    print("Errou!")
    usuario = input("informe seu usuário: ").upper()
    senha = input("informe sua senha: "). upper()
else:
    (print(" Seja bem vindo!", usuario))
    
    
