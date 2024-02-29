num1 = int(input("Digite un número"))
num2 = int(input("Digite otro número"))

if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
    suma = num1 + num2
    if (suma % 2 == 0):
        print("La suma es par" )
else:
    print ("La suma no es par")
            
