sálario = int(input("Informe um sálario:"))
financiamento = int(input("Informe financiamento pretendido:"))

fin = (financiamento * 5)

if sálario<fin:
    print(f"Financiamento concedido\n")

elif sálario>fin:
    print(f"Financiamento negado\n")

else:
    print("Obrigado por nos consultar")