#Exercício 1

ano = int(input('Qual o seu ano de nascimento? '))
idade = 2025 - ano
print('A sua idade é: ' + str(idade))

#Exercício 2

car = float(100.00)
cliente = int(input('Quantos carros você quer alugar? '))
total = car*cliente
print('O valor total é: ' + str(total))

#Exercicio 3

tempC = float(input('Digite a temperatura em Celsius: '))
tempF = (tempC*9/5) + 32
print('A temperatura em fahrenheit é: ' + str(tempF))

#Exercício 4

nota1 = float(input('Digite a sua nota: '))
nota2 = float(input('Digite a sua nota: '))
nota3 = float(input('Digite a sua nota: '))
nota4 = float(input('Digite a sua nota: '))
med = ((nota1 + nota2 + nota3 + nota4)/4)
print('A média das notas é: ' + str(med))

#Exercício 5

idade = int(input('Qual a sua idade? '))
mesTotal = idade*12
print('A sua idade em meses é: ' + str(mesTotal))

#Exercício 6

peso = float(input('Quantos kilos de picanha? '))
valor = float(59.99*peso)
print('O preço total é: ' + str(valor))