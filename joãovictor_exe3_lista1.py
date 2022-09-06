#reducao_de_tempo_de_vida

cigarros = int(input("Quantidade de cigarros fumados por dia:"))
anos =float(input("Quantos anos fumou:"))

#calculo
dias = (anos * 365 * cigarros) * 10 / 24

print("A quantidade de dias perdidos é: ",dias)