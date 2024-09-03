nome = input("Informe seu nome: ")
end = input("Informe seu endereço: ")
idade = input("Informe seu idade: ")

# Exibindo dados das variáveis
#print(nome, end, idade)

#1 forma de concatenação
print("\nOlá ",nome, " seu endereço é ",end, " sua idade é ", idade)

#2 forma de concatenação
print("\nOlá {} seu endereço é {} e sua idade é {}".format(nome, end, idade))

#3 forma de concatenção - f string
print(f"Bem vindo {nome}, você mora na {end} e tem {idade} anos")