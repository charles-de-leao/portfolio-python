#exercício número 5 - Inverter caracteres

def inverter_caracter(palavra):
    return palavra[::-1]

palavra = str(input('Digite uma falavra ou frase para ser invertida: '))

print(inverter_caracter(palavra))