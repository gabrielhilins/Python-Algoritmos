altura = float(input("Qual sua Altura:"))
sexo = input("Qual seu sexo (M ou F):")

if sexo == "M" :
    peso_ideal = (72.7 * altura) - 58
    print(peso_ideal)
else :
    peso_ideal = (62.1 * altura) - 44.7
    print(peso_ideal)