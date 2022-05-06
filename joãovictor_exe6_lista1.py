#Calculo IMC

peso = float(input('Digite o seu peso em quilos (Ex.: 77):'))  
altura = float(input('Digite a sua altura em metros (Ex.: 1.85):'))  

#Execução do cálculo 
#Fórmula: Peso dividido pela altura ao quadrado
imc = peso / (altura * altura)


#IMC
print('Seu IMC (índice de massa corporal) é: ',imc)

#tabela de referência

print('Tabela de referência')

print('IMC abaixo de 18,5kg/m2            | Baixo peso')
print('IMC de 18,5 e menor que 24,9kg/m2  | Peso normal')
print('IMC de 24,9 e menor que 29,9kg/m2  | Sobrepeso')
print('IMC de 29,9 e menor que 31,56kg/m2  | Obesidade Grau I')
print('IMC de 34,9 e menor que 39,9kg/m2  | Obesidade Grau II')
print('IMC maior ou igual a 39,9kg/m2     | Obesidade Grau III')


#resultado
print('Seu resultado:')

#IMC abaixo de 18,5kg/m2            | Baixo peso
if float(imc) < float(18.5):
  print('Baixo peso')

#IMC de 18,5 e menor que 24,9kg/m2  | Peso normal
if float(imc) > float(18.5) and float(imc) < float(24.9):
  print('Peso normal')

#IMC de 24,9 e menor que 29,9kg/m2  | Sobrepeso
if float(imc) > float(24.9) and float(imc) < float(29.9):
  print('Sobrepeso')

#IMC de 29,9 e menor que 31,56kg/m2  | Obesidade Grau I
if float(imc) > float(29.9) and float(imc) < float(31.56):
  print('Obesidade Grau I')

#IMC de 34,9 e menor que 39,9kg/m2  | Obesidade Grau II
if float(imc) > float(34.9) and float(imc) < float(39.9):
  print('Obesidade Grau II')

#IMC maior ou igual a 39,9kg/m2     | Obesidade Grau III
if float(imc) >= float(39.9):
  print('Obesidade Grau III')



