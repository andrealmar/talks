# Este programa é uma simples calculadora que contém as principais operações matemáticas:
# adição, subtração, multiplicação e divisão
# baseado no código disponível em: http://www.programiz.com/python-programming/examples/calculator

# Função SOMA
def add(x, y):
   """Função que SOMA dois números"""
   return x + y

# Função SUBTRAÇÃO
def subtract(x, y):
   """Função que SUBTRAI dois números"""
   return x - y

# Função MULTIPLICAÇÃO
def multiply(x, y):
   """Função que MULTIPLICA dois números"""
   return x * y

# Função DIVISÃO
def divide(x, y):
   """Função que DIVIDE dois números"""
   return x / y

# Pede ao usuário que selecione uma operação: (SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO ou DIVISÃO)
print(" Selecione uma operação matemática: ")
print("1.SOMA")
print("2.SUBTRAÇÃO")
print("3.MULTIPLICAÇÃO")
print("4.DIVISÃO")

choice = input("Digite a sua escolha: (1/2/3/4):")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("ERRO!!!")
