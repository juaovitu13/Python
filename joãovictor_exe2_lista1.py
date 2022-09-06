#carro_alugado

km = float(input("Quantidade de kms percorridos:"))
dias = float(input("Quantidade de dias:"))

#execução_do_calculo

total = (dias * 60) + (km * 0.15)

print("O total a pagar é: ",total)