
alt = input("digite sua altura: ")
pes = input("digite seu peso: ")

altu = float(alt)
peso = float(pes)

calculo = peso / altu**2

resultado = int(calculo)
                                 #pode tirar o < pq nao precisa: resultado < 25
if resultado < 18.5:
    print("you are underweight")
elif  18.5 < resultado < 25:
    print("you have normal weight")
elif 25 < resultado < 30:
    print("you are overweight")
elif 30 < resultado < 35:
    print("you are obese")
else:
    print("you are clinically obese")
