# api do tipo soap
# api do tipo rest

import requests

parametros ={
    "nome":"Batman",
    "idade": 80,
    "endereco": "Bat-el"
}

payload ={
    "regiao": 1,
    "marca": "renault",
    "preco":"50000"
}

headers = {
    "token": "batata",
}
# response = requests.get("https://httpbin.org/get", params = parametros)
response = requests.post("https://httpbin.org/post", json=payload, headers=headers)

print(response)
print(response.text) # irá me retornar o corpo do conteudo solicitado
print("JSON ->", response.json())
print(response.status_code) # retrona um inteiro (ex: cod 200) como resposta
print(response.headers) # me retorna cabeçalho da requisição.(metadados da conexão)

