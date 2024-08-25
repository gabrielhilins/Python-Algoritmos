peso = float(input("Qual seu Peso:"))
altura = float(input("Qual sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5 :
    print("Você está ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25 :
    print("Você esá PESO NORMAL")
elif imc >= 25 and imc < 30 :
    print("Você está ACIMA DO PESO")
else:
    print("Você está OBESO")