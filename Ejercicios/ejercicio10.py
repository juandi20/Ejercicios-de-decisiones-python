import math

num = int(input("Por favor, Digite un número"))

if (num > 9 and num < 100):
    digito1 = math.trunc(num / 10)
    digito2 = num % 10

    if (digito1 == digito2):
        print ("Los digitos son iguales")
    else:
        print("Los digitos no son iguales")