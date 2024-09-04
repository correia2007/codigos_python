sexo = float(input("Digite 1 para homen ou 2 para mulher:"))
altura = float(input("Digite sua altura:"))

if sexo == 1:
    conta = ((72.7 * altura) - 58)
    
if sexo == 2:
    conta = ((62.1 * altura) - 44.7)
print(f"Seu peso ideal {conta} \n")