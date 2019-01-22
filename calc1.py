def add(c):
    c = c + a
    return c

def sub(c):
    c = c + a
    return c

def mul(c):
    c = c + a
    return c

def div(c):
    c = c + a
    return c

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4/5):")
if choice == '1':
    a = int(input("enter number: "))
    x = []
    x.insert(a)
    print(add(a))
