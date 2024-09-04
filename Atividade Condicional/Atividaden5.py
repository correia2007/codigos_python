km = float(input("quantos Kms irão percorrer?"))
carro = int(input("qual o modelo do carro 1, 2 ou 3?"))

if carro ==1:
    cec= (km/8)
    print(f"O consumo estimado vai ser de {cec:.2f}")
elif carro ==2:
    cec= (km/9)
    print(f"O consumo estimado vai ser de {cec:.2f}")
elif carro ==3:
    cec= (km/12)
    print(f"O consumo estimado vai ser de {cec:.2f}")
