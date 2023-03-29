string = input("Digite uma string: ")

# Converter a string em uma lista de caracteres
lista_caracteres = list(string)

# Inverter a lista de caracteres
for i in range(len(lista_caracteres) // 2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[len(lista_caracteres) - i - 1]
    lista_caracteres[len(lista_caracteres) - i - 1] = temp

# Converter a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

print("String invertida: ", string_invertida)