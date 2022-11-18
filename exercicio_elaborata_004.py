""" Dada a String" houveram 12325 visitantes" crie uma nova lista contendo apenas digitos"""

texto =("houveram 12325 visitantes")

"""lista = []
for numero in texto:
    if numero.isdigit():
        lista.append(numero)

print(sorted(lista))"""

numeros = [numero for numero in texto if numero.isdigit()]

print(sorted(numeros))