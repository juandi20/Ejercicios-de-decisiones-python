import math

num = int(input("Por favor, Digite un número"))

if (num > 9 and num < 100):
    digito1 = math.trunc(num / 10)
    digito2 = num % 10
    es_primo = True

    for i in range(2, digito1):
        if digito1 % i == 0:
            es_primo = False
            break
        
    for i in range(2, digito2):
        if digito2 % i == 0:
            es_primo = False
            break

    print("los dos digitos son primos" if es_primo else "no son primos")