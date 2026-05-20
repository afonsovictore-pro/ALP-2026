
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input("Quantos números quer digitar?"))
contador = 0 # o contador tinha que estar no zero
impares = 0

while contador < N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
        contador += 1 # nao tinha o contador dentro do while

print(f"Quantidade de ímpares entre 1 e {N}: {impares}")
