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

#python numbers
x = 1 #int
y = 2.5 #float
z = 1j #complex
print("Python has different numbers...")
print(x, " is an integer number")
print(y, " is a float number")
print(z, " is a complex number")

#multiline string using three quotes or three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are Arrays
a = "Hello, World!"
print(a[5]) #print that character
print(len(a)) #print string length using len()
print("Hello" in a) #check if "Hello" is present
if "Hello" in a: #check IF
    print("Hello is present in the string.")
if "Bye" not in a: #check IF NOT
    print("Bye is not present in the string")   
 

#we can also loop through the String
for x in "Banana":
    print(x)

#Slicing
#return a range of characters from a string using slice syntax
b = "Hello, World!"
print("b = " + b)
print("b[2:5] = " + b[2:5])
print("b[:5] = " + b[:5]) #slice from beginning
print("b[2:] = " + b[2:]) #slice to the end
print("b[-5:-2] = " + b[-5:-2]) # negative indexing from -5 from the end 'o' to -2 from the end 'd'

print("Using uppercase method: " + b.upper())   #using uppercase method
print("Using lowercase method: " + b.lower())   #using lowercase method
b = "    Hello, World!   "
print("Removing whitespace: " + b.strip())      #removing whitespace
b= "Hello, World!"
print("Using replace method: " + b.replace("H", "J"))   #using replace method
b = "Hello, World!"
print("Using split method: " , b.split(","))    #using split method

#Format String
age = 36
txt = "My name is John, and I am {}"
print("\nage = " , age)
print("txt = " + txt)
print("txt.format(age) = ", txt.format(age))

#unlimited numbers can be formated
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."

print("quantity = 3 itemno = 567 price = 49.95")
print('myorder = "I want {} pieces of item {} for {} dollars."')
print("myorder.format(quantity, itemno, price) = ", myorder.format(quantity, itemno, price))

#we can also place index numbers
print("\nWe can also use index numbers!")
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print('myorder = "I want to pay {2} dollars for {0} pieces of item {1}"', myorder.format(quantity, itemno, price))


