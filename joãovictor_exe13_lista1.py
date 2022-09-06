#5 pessoas

#quantidade de pessoas com mais de 50 anos
QtdPessoasMaiorCinquenta = 0

#média da altura das pessoas entre 10 e 20 anos
QtdPessoasEntre10e20 = 0
SomaAlturaPessoasEntre10e20 = 0

#percentual de pessoas com peso inferior a 40 kg
QtdPessoasPesoMenor40 = 0

#coletar dados de 5 pessoas
for i in range(5):
    print("Pessoa ", i + 1)

    idade = int(input("Informe a idade:"))
    altura = float(input("Informe a altura:"))
    peso = float(input("Informe o peso:"))
    
#pessoas com idade maior que 50 anos
    if int(idade) > int(50):
      QtdPessoasMaiorCinquenta = QtdPessoasMaiorCinquenta + 1

#média de altura de pessoas entre 10 e 20 anos
    if int(idade) >= int(10) and int(idade) <= int(20):
      QtdPessoasEntre10e20 = QtdPessoasEntre10e20 + 1
      SomaAlturaPessoasEntre10e20 = SomaAlturaPessoasEntre10e20 + altura

#pessoas com peso inferior a 40 kg
    if int(peso) < int(40):
      QtdPessoasPesoMenor40 = QtdPessoasPesoMenor40 + 1

    print("----------------")


print("Resultados obtidos:")


print("Número de pessoas com mais de 50 anos: ", QtdPessoasMaiorCinquenta)

#divisão por zero, caso nenhuma pessoa esteja na faixa de 10 aos 20 anos
if int(QtdPessoasEntre10e20) == 0:
  print("Não foram informadas pessoas na faixa dos 10 aos 20 anos.")
else:
  print("Média de altura das pessoas entre 10 e 20 anos: ", SomaAlturaPessoasEntre10e20 / QtdPessoasEntre10e20, "mt")

#divisão por zero, caso nenhuma pessoa tenha menos de 40 kg
if int(QtdPessoasPesoMenor40) == 0:
  print("Percentual de pessoas com menos de 40 kg: 0%")
else:
  print("Percentual de pessoas com menos de 40 kg: ", int(100 /  5 * QtdPessoasPesoMenor40), "%")