# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
print("\n Selecione o número da operação desejada: ")

print(" 1 - Soma")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")

def soma(num1,num2):
    resultadoSoma = num1 + num2
    mensagem = f"{num1} + {num2} = {resultadoSoma}"
    print(mensagem)

def subtracao(num1,num2):
    resultadoSubtracao = num1 - num2
    mensagem = f"{num1} - {num2} = {resultadoSubtracao}"
    print(mensagem)

def multiplicacao(num1,num2):
    resultadoMultiplicacao = num1 * num2
    mensagem = f"{num1} * {num2} = {resultadoMultiplicacao}"
    print(mensagem)

def divisao(num1,num2):
    if num2 == 0:
       mensagem = "Não é possível realizar divisões por 0!"
    else:
         resultadoDivisao= num1 / num2
         mensagem = f"{num1} / {num2} = {resultadoDivisao}"

    print(mensagem)

opcao = int(input("\n Digite a sua opção: (1/2/3/4): "))
if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
    print("Por favor, escolha uma opção válida (1/2/3/4)!")

num1 = int(input('\n Digite o primeiro número: '))
num2 = int(input('\n Digite o segundo número: '))

if opcao == 1:
    soma(num1, num2)
elif opcao == 2:
    subtracao(num1,num2)
elif opcao == 3:
    multiplicacao(num1,num2)
elif opcao == 4:
    divisao(num1,num2)