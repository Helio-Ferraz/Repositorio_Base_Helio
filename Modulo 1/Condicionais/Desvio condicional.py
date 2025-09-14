



Aluno = input("Qual seu nome?")
Prova1 = float(input("Qual sua nota da prova1 ?"))
Prova2 = float(input("Qual sua nota da prova2 ?"))
Prova3 = float(input("Qual sua nota da prova3 ?"))


Média = float(Prova1 + Prova2 + Prova3) / 3
print(Média)


if Média >= 7:
    print("Aprovado")
elif Média <= 5:
    print("Recuperação")
else:
    print("reprovado")