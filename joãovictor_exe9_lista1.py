#Coleta de dados
PrimeiroNumero = float(input("Informe o primeiro número: "))
SegundoNumero =  float(input("Informe o segundo número: "))

#operação
print("")
print("Operações disponíveis:")
print("1 - Elevar o primeiro número ao segundo número;")
print("2 - Raiz quadrada de cada um dos números;")
print("3 - Raiz cúbica de cada um dos números.")
print("")
Operacao =  input("Digite o número referente à uma das operações anteriores: ")
print("")

if Operacao not in("1","2","3"):
  print("Operação inválida!")  
  exit()


# 1 - Elevar o primeiro número ao segundo número
if Operacao == "1":  
  print("Resultado da operação de elevação: ", PrimeiroNumero ** (SegundoNumero))

# 2 - Raiz quadrada de cada um dos números
elif Operacao == "2":
  print("Raiz quadrada do primeiro número: ", PrimeiroNumero ** (1/2))
  print("Raiz quadrada do segundo número: ", SegundoNumero ** (1/2))

# 3 - Raiz cúbica de cada um dos números
elif Operacao == "3":
  print("Raiz cúbica do primeiro número: ", PrimeiroNumero ** (1/3))
  print("Raiz cúbica do segundo número: ", SegundoNumero ** (1/3))