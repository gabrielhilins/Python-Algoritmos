produto = input("Digite o nome do produto:")
preco_etiqueta = float(input(f"Qual o preço do produto {produto}:"))
print("Formas de Pagamento:")
print("Dinheiro/Cheque, Cartao de Credito, Parcelado 2x e Parcelado 3x")
forma_pagamento = input("Qual vai ser a Forma de Pagamento:")

if forma_pagamento == "Dinheiro/Cheque" :
    preco_pago = preco_etiqueta - (preco_etiqueta * 0.10)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago)
elif forma_pagamento == "Cartao de Credito" :
    preco_pago = preco_etiqueta - (preco_etiqueta * 0.15)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago)
elif forma_pagamento == "Parcelado 2x" :
    preco_pago = preco_etiqueta
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago) 
else :
    preco_pago = preco_etiqueta + (preco_etiqueta * 0.10)
    print("Produto: ", produto)
    print("Forma de Pagamento: ", forma_pagamento)
    print(f"Preço a ser Pago: ", preco_pago) 
   

