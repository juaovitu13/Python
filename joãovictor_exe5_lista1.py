#quantidade de cedulas

a = int(input("Coloque o valor:"))
print("---------")

#calculos

cedula100 = a / 100
a = a - cedula100 * 100

cedula50 = cedula100 * 2

cedula20 = a / 20

cedula10 = a / 10

cedula5 = cedula10 * 2

cedula2 = cedula10 * 5

cedula1 = a 

print("{}nota(s) de 100,00",cedula100)
print("{}nota(s) de 50,00",cedula50)
print("{}nota(s) de 20,00",cedula20)
print("{}nota(s) de 10,00",cedula10)
print("{}nota(s) de 5,00",cedula5)
print("{}nota(s) de 2,00",cedula2)
print("{}nota(s) de 1,00",cedula1)