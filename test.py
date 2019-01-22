from test2 import Test

a = Test
b = a()
c = Test()

print("Type of a: " + str(type(a)))
print("Type of b: " + str(type(b)))
print("Type of c: " + str(type(c)))
print(a is b)
print(b is c)
print(c is a)
