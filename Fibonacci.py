num = int(input("Enter the Number:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    next = n1 + n2
    n1 = n2
    n2 = next
    print(next, end=" ")


print()