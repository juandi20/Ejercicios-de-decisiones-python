num = int(input("Por favor, Digite un número"))

if (num < 0):
    print('El número es negativo por lo tanto no puede ser primo')
if (num >= 10 and num <= 20):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print ('El número es primo.')
    else:
        ('El número no es primo.')    
else: 
    print('El número no es menor a 20')        