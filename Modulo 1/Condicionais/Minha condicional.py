



Nome = input("Qual seu nome de usuario?")
Idade = int(input("Qual sua idade?"))

if Idade >= 18:
    print("\nMaior de idade")
else:
    print("\nMenor de idade")


print("\n-----------------------------")


jogo = input("Qual jogo você vai jogar?")
if jogo == "Cod_war":
    print("\ncarregando...")
    sensibilidade = float(input("Qual sensibilidade você vai usar?"))
    if sensibilidade <= 0.99:
        print("Sensibilidade baixa.")
    elif sensibilidade >= 1.0:
        print("Sensibilidade alta.")
    else:
        print("Sensibilidade trabalha com numeros, idiota")
