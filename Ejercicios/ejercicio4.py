import math

num = int(input("Por favor, Digite un número"))

if (num > 9 and num < 100):
    digito1 = math.trunc(num / 10)
    digito2 = num % 10
    suma = digito1 + digito2

    print('la suma de los digitos es: ', suma)

else:
    print('El número no es de dos digitos')