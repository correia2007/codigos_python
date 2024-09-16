programa = 0

while True:
    valor = int(input("digite um valor:"))
    if valor == 0:
        break
    if valor % 2 != 0:
        programa += 1

print(f"Quantidade de números impares digitados: {programa}")