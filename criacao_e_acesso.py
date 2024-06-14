# dados = dict(nome="Aiko", idade= 23)
# print (dados)

# dados["telefone"] = "981918004"
# print (dados)

# dados["telefone"] = "30000000"
# print (dados)


dados_clientes = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone": "10000000"},
    "aiko@gmail.com":{"nome":"Aiko", "telefone": "20000000"},
    "fatima@gmail.com":{"nome":"Fatima", "telefone": "30000000"},
    "kamille@gmail.com":{"nome":"Kamille", "telefone": "40000000"},
}

# nomes_clientes = [
#     dados_clientes["aiko@gmail.com"]["nome"],
#     dados_clientes["guilherme@gmail.com"]["nome"],
#     dados_clientes["fatima@gmail.com"]["nome"],
#     dados_clientes["kamille@gmail.com"]["nome"],
# ]
# print (nomes_clientes)

for chave, valor in dados_clientes.items():
     print (chave, valor)

