print ("Escola")
print ("--------------")
NOME = input("Digite o nome do aluno: ")
BIM1 = float(input("Digite a nota do primeiro bimeste: "))
BIM2 = float(input("Digite a nota do segundo bimeste: "))
BIM3 = float(input("Digite a nota do terceiro bimeste: "))
BIM4 = float(input("Digite a nota do quarto bimeste: "))
MEDIA = ((BIM1+BIM2+BIM3+BIM4)/4)
print ( NOME, "Sua nota foi: ", MEDIA)
if MEDIA >= 9:
    print ("Aproado com Louvor") 
elif MEDIA >= 7:
    print ("Aprovado") 
elif MEDIA < 7:
    print ("Reprovado")