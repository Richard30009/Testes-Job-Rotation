penultimo = 0 
ultimo = 1
indice = 0



numero = int(input(" Digite um numero para verificarmos se ele pertence a sequencia Fibonacci: "))

while (numero > indice):
    indice = ultimo + penultimo
    penultimo = ultimo
    ultimo = indice
    print(indice)

if numero == indice:
    print('O numero {} faz parte da sequencia Fibonacci!'.format(numero))
else:
    print('O numero {} nao pertence a sequencia Fibonacci!'.format(numero))
    print('Como podemos ver os numeros mais proximos sao {}'.format(indice))
    indice = penultimo
    print('e {}'.format(indice))

