
# Calculadora Versão 2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

def adicao (a, b):
    return (a + b)

def subtracao (a, b):
    return (a - b)

def multiplicacao (a, b):
    return (a * b)

def potenciacao (a, b):
    return (a ** b)

def media (a, b):
    return (a + b)/2

def diferenca(a, b):
    return a - b

def produto (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        print("Escreva um numero maior que 0")
    else:
        return a/b 
    
operacoes = {
    
    1: adicao,
    2: subtracao,
    3: divisao,
    4: multiplicacao,
    5: potenciacao,
    6: media,
    7: diferenca,
    8: produto,

}

print("\nOperadores \n1: Adição \n2: Subtração \n3: Divisão \n4: Multiplicação \n5: Potenciação \n6: Media \n7: Diferença \n8: Produção ")

escolha = int(input('escolha um número entre 1 e 8: '))

if escolha not in [1, 2, 3, 4, 5, 6, 7, 8]:
    print('escolha um número válido')
else:
    resultado = operacoes.get(escolha)
    print(resultado(n1,n2))