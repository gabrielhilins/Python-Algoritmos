a1 = int(input("Digite o valor Inicial (A1):"))

r = int(input("DIgite o valor da Razão R:"))

print("Sequência em P.G. com 10 valores:")

for n in range(10) :
    an = a1 * (r ** (n - 1))
    print(an)