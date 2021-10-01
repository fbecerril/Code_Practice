#python basics based on w3.schools.com
#Creating Variables
x = 5
y = "John"
print(x)
print(y)

#casting
x = str(3)
y = int(3)
z = float(3)

#using type()
print(type(x))
print(type(y))
print(type(z))

#case sensitivity
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#python allows assignment of values to multiple variables
x, y, z = "Orange", "Banana" ,"Cherry"
print(x)
print(y)
print(z)

#..also same value to multiple variables
x = y = z = 1

#python allows a collection of valies to be unpacked 
fruits = ["apple", "bannana", "cherry"]
x, y, z = fruits
print(x); print(y); print(z) #we can also have multiple prints in one line

#output variables
x = "awesome"
print("python is " + x)



