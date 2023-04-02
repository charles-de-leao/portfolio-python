# exercício número 2 - Fibonacci

n = int(input("Digite o número que deseja verificar: "))

sequencia = []
ultimo = 1
penultimo = 0

contagem = 1
while True:
    if contagem <= n:
        valor = ultimo + penultimo
        penultimo = ultimo
        ultimo = valor
        contagem += 1
        sequencia.append(valor)

    else:
        break

if n in sequencia:
    print(f'O número {n} está presente na Sequência de Fibonacci.')
    print(sequencia)

else:
    print(f'O número {n} não está presente na Sequência de Fibonacci.')
    print(sequencia)






