salário = int(input("Informe o salário do funcionário:"))

if salário <600:
    sal= salário * 1.3
    print(f"Seu sálario teve aumento de 30%, ficando: {sal}\n")

else:
    print(f"Seu sálario {salário} não teve aumento\n")