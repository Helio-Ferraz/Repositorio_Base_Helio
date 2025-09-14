nome = input("Qual seu nome?")
peso = float(input("Quanto você pesa ?"))
altura = float(input("Qual sua altura ?"))
resultado = peso / (altura * altura)
print(resultado)

if resultado < 18.5:
    print("Abaixo do peso")
elif resultado <= 24.9:
    print("Peso normal")
elif resultado <= 29.9:
    print("Sobrepeso")
elif resultado <= 34.9:
    print("Obesidade grau 1")
elif resultado <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")