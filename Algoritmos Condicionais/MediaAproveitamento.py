id_aluno = int(input("Qual o Número de Identificação do aluno: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Verifica se alguma nota é menor que zero
if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print("Nota menor que zero. Tente novamente.")
else:
    # Calcula a média e a média de aproveitamento
    media = (nota1 + nota2 + nota3) / 3
    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media) / 7

    # Definindo o conceito com base na média de aproveitamento
    if media_aproveitamento >= 90:
        conceito = "A"
    elif media_aproveitamento >= 75:
        conceito = "B"
    elif media_aproveitamento >= 60:
        conceito = "C"
    elif media_aproveitamento >= 40:
        conceito = "D"
    else:
        conceito = "E"

    # Definindo a situação acadêmica com base no conceito
    if conceito == "A" or conceito == "B" or conceito == "C":
        situacao = "Aprovado!"
    else:
        situacao = "Reprovado!"

    # Imprimindo os resultados
    print("Número de Identificação: ", id_aluno)
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Nota 3: ", nota3)
    print("Média: ", media)
    print("Média de Aproveitamento: ", media_aproveitamento)
    print("Conceito: ", conceito)
    print("Situação Acadêmica: ", situacao)
