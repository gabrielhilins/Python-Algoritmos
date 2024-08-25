nome = input("Digite seu nome:")
sexo = input("Digite seu sexo (M ou F):")
estadoCivil = input("Digite seu Estado Civil:")
if estadoCivil == "Casada" and sexo == "F":
    tempoCasamento = int(input("Quantos anos de Casamento?"))
    print(nome, sexo, estadoCivil, tempoCasamento)
else :
    print(nome, sexo, estadoCivil)