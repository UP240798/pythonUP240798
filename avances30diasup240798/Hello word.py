# Exercise 1. Operations

print(3 + 4)
print (3 - 4)
print (3 * 4)
print (3 % 4)
print (3 / 4) 
print (3 ** 4)
print (3 // 4)

# Now i write strings on the python interactive shell

print ("My name is Emilio Fernando ") 
print ("My family name is Gutierrez Rodriguez")
print ("My country is Mexico")
print ("I am enjoying 30 days of python")

# Check the data types of the following data
print (type(10))
print (type(9.8))
print (type(3.14))
print (type(4-4j))
print (type(['Asabeneh','Python','Finland']))
print (type("My name is EMilio fernando"))
print (type("My family name is Gutierrez Rodriguez"))
print (type("My country is Mexico"))

#Exercise 3. Examples

# Number Types
integer_num = 10                # Integer
float_num = 3.14                # Float
complex_num = 2 + 3j            # Complex

# String Type
name = "Hello, word"         # String

# Boolean Type
is_valid = True                 # Boolean

# List Type (ordered, mutable, allows duplicates)
fruits = ["apple", "banana", "cherry"]

# Tuple Type (ordered, immutable, allows duplicates)
coordinates = (4.5, 6.7)

# Set Type (unordered, mutable, no duplicates)
unique_numbers = {1, 2, 3, 2, 1}   # Output will be {1, 2, 3}

# Dictionary Type (key-value pairs)
person = {
 "name": "Alice",
    "age": 25,
    "is_student": False
    }

#2.
import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance:", distance)