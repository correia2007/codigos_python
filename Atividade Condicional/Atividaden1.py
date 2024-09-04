valor = int(input("Informe um valor numérico:"))

if valor >=100 and valor <=200:
    print(f"Este valor {valor} está entre 100 e 200\n")
elif valor < 100:
    print(f"Este valor {valor} não está entre 100 e 200\n")
else:
    print(f"O número {valor} é maior que 200\n")