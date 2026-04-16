num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))

def GCD(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 > num2:
        return GCD(num1 - num2, num2)
    else:
        return GCD(num1, num2 - num1)

result = GCD(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)