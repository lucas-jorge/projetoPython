""" # 1 - Imprima a frase: Python na Escola de Programação da Alura.

print('Python na Escola de Programação Alura')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = ('Lucas')
idade = 37
print('Meu nome é {nome} e tenho {idade} anos')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print('A','L','U','R','A',sep='\n')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável 
# e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

# Lista com quatro nomes;
nomes = ['Lucas', 'Ana', 'Maria', 'João']
print(nomes)

# Lista com o ano que você nasceu e o ano atual.
anos = [1986, 2024]
print(anos)

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in numeros:
    print(numero)
# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for numero in numeros:
    if numero % 2 != 0:
        soma += numero
print(soma) """

#  Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
# for numero in range(10, 0, -1): # range(10, 0, -1) gera uma sequência decrescente de 10 a 1
#    print(numero)

""" num = int(input('Digite um número para ver sua tabuada: '))

for numero in range(1, 11):
    resultado = num * numero
    print(f'{num} x {numero} = {resultado}') """
    
# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for numero in numeros:
    try:
        soma += numero
        print(f'A soma dos números é: {soma}')
    except Exception as e:
        print(f'Erro: {e}') """
        
# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = []
soma = 0

for numero in numeros:
    soma += numero
    
try:
    media = soma / len(numeros)
    print(f'A média dos números é: {media}')
except ZeroDivisionError:
    print('Não é possível calcular a média de uma lista vazia')
except Exception as e:
    print(f'Erro: {e}')
        