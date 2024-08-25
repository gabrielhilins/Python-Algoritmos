n = int(input("Digite um valor:"))

if n < 1 :
    print("Número menor que 1 ou maior que 10. Tente Novamente")
else:
    for i in range(1, 11):
        tabuada = n * i
        print(i, " X ", n, " = ", tabuada)
