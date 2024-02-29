import math

num = int(input("Por favor, Digite un número"))

if (num > 9 and num < 100):
    digito1 = math.trunc(num / 10)
    digito2 = num % 10
    if(digito1 % 2 == 0 and digito2 % 2 == 0):
        print('Los dos digitos son pares')
    else:
         print('Alguno de los digitos no es par')
else:
	print('El número es de dos digitos')		