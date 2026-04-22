peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura **2)
if imc > 30.3:
    print ("Cuidado com a saúde")
else:
    print ("Tudo ok")

if imc < 18.5:
    print ("Abaixo do peso")
elif imc < 24.9:
    print ("Peso normal")
if imc < 29.9:
    print ("Sobrepeso")
elif imc < 34.9:
    print ("Obesidade Grau 1")
if imc < 39.9:
    print ("Obesidade Grau 2")
else:
    print ("Obesidade Grau 3 (mórbida)")    