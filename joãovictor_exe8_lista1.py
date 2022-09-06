#tempo de jogo

horaI = int(input("Coloque a hora inicial:"))
minutoI = int(input("Coloque o minuto inicial:"))
horaF = int(input("Coloque a hora final:"))
minutoF = int(input("Coloque o minuto final:"))

#variaveis
resul = 0
tempo = 0

if (horaF > horaI): 
  tempo = horaF - horaI

elif (horaF < horaI):
  tempo = (24 - horaI) + horaF

elif (horaF == horaI):
  tempo = 24

if (minutoF < minutoI):
  resul = (60 - minutoI) + minutoF

elif (minutoF > minutoI):
  resul = minutoF - minutoI

elif (minutoF == minutoI):  
  resul = 60

elif (minutoI == 0):
  resul = minutoF + 0

elif (minutoI == 0):
  resul = minutoI + 0

total = (tempo * 60) + resul
if (total > 1440):
  print("O jogo ultrapassou o limite de 24 Horas")


print("O jogo durou",tempo ,"hora(s) e",resul ,"minuto(s)")
