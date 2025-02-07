x = 5
y = "John"
print(x)
print(y)

a = str(5)
b = int(3)
c = float(2)
print(type(a))
print(type(b))
print(type(c))

###Naming strategies
myVariable = 1 #camelCase
MyVariable = 1 #PascalCase
my_variable = 1 #snake_case

i, j, k = 1, "two", float(3)
print(i)
print(j)
print(k)

X = "Python"
Y = "is"
Z = "awesome"
print(X, Y, Z)



### ^ These are global variables, because they were defined outside of function

x = "awesome"
def myFunc ():
  x = "fantastic"
  print("Python is", x)

myFunc()
print("Python is", x)