contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

print("="*40)

valor = 0
while valor >=0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar):"))

    print(f"Você digitou {valor}")

print("="*40)

while True:
    senha = input("Informe a senha: ")
    if senha == "123":
        print("Parabens, Senha correta")
        break #forma de encerrar o while
    else:
        print("Senha incorreta, tente novamente")