
lista =list(range(1,51,))
print(lista)

"""lista_impar = []

for impar in lista:
    if impar % 2:
        lista_impar.append(impar)
        
print(lista_impar)"""

lista_impar =[ impar for impar in lista if impar %2]
print(lista_impar)

