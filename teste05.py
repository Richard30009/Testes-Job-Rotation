invertida = ""
frase = input('Digite uma frase ou uma palavra: ')
for palavra in frase.split(" "):
    invertida += palavra[::-1]+" "
print('A frase que você digitou invertida fica: {}'.format(invertida))