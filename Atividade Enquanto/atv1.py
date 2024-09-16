print("="*40)

print("Cadastro do Primeiro usuario.")

print("="*40)

while True:
    loginPU = input("login:")
    senhaPU = input("senha:")
    if loginPU != senhaPU:
        break
    print("O login e a senha não podem ser iguais. Tente novamente.")


print("="*40)

print("Cadastro do Segundo usuario.")

print("="*40)

while True:
    loginSU = input("login:")
    senhaSU = input("senha:")
    if loginSU != senhaSU and loginSU != loginPU:
        break
    if loginSU == senhaSU:
        print("O login e a senha não podem ser iguais. Tente novamente.")
    else:
        print("O login do primeiro usuario e o do segundo usuario não podem ser iguais. Tente novamente")

print("="*40)

print("Cadastros bem sucedidos!")