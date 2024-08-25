a = int(input("Digite um valor inteiro A:"))
b = int(input("Digite um valor inteiro B:"))
c = int(input("Digite um valor inteiro C:"))

if a != b and a != c and b != c:
    valores = [a, b, c]
    ordenados = sorted(valores)
    print(ordenados)
else :
    print("Algum ou Alguns valores sao Iguais. Tente Novamente")
