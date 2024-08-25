a = int(input("Digite o valor que voce deseja saber o Fatorial dele:"))

resultado = 1
sequencia = []

for i in range(a, 0, -1) :
        resultado *= i
        sequencia.append(i)

print(a, "! =", resultado)