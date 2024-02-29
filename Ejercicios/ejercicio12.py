import math

num1 = int(input("Digite un número"))
num2 = int(input("Digite otro número"))

def tienen_digitos_comunes(num1, num2):
    if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
        di1_num1 = math.trunc(num1 / 10)
        di2_num1 = num1 % 10

        di1_num2 = math.trunc(num2 / 10)
        di2_num2 = num2 % 10

        if di1_num1 == di1_num2 or di1_num1 == di2_num2 or di1_num2 == di1_num1 or di1_num2 == di2_num2:
            return True
        else:
            return False
if tienen_digitos_comunes (num1, num2):
    print ("Los números tienen digitos iguales")
else:
    print ("Los números no tienen digitos iguales")    