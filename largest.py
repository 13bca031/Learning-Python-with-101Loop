a = float(input("enter 1 number: "))
b = float(input("enter 2 number: "))
c = float(input("enter 3 number: "))

if c <= a >= b:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c

print("largest among 3 number is: ",largest)
