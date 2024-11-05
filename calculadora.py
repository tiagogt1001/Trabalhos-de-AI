from unittest import removeResult


def soma (x,y):
    return x+y

def subtracao (x,y):
    return x-y

def divisao (x,y):
    return x/y

def multiplicacao (x,y):
    return x*y

def calculadora():
    lista_contas = []

    while True:
                num1 = int(input("digite o primeiro numero: "))
        num2 = int(input("digite o segundo numero: "))
        op = input("Digite a operação: ")

        if op == "soma":
           result = soma(num1, num2)
           print("Resultado da soma:" + str(result))
           lista_contas.append(str(num1) + "+" + str(num2) + "=" +str(result))

        elif op == "multiplicação":
            result = multiplicacao(num1, num2)
            print("Resultado da multiplicação:" + str(result))
            lista_contas.append(str(num1) + "*" + str(num2) + "=" + str(result))
        elif op== "divisão":
            result = divisao(num1, num2)
            print("Resultado da divisão:" + str(result))
            lista_contas.append(str(num1) + "/" + str(num2) + "=" + str(result))
        elif op== "subtração":
            result = subtracao(num1, num2)
            print("Resultado da subtração:" + str(result))
            lista_contas.append(str(num1) + "-" + str(num2) + "=" + str(result))
        else :
            print("Nem tu sabes quanto é, como é que é suposto eu saber?")
            print(lista_contas)

calculadora()

