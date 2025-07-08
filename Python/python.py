#Numeric Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

# Int num = 3
# Float num = 3

#Variables

my_variable = 10
total_count = 0
user = 'John'

# Invalid
second_variable = 10
user_name = 20

#Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponents (**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

x = 10
x += 2
x -= 2
x *= 2
x /= 2
x %= 2
x **= 2

print(x)

#Operators with strings

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2)

print(str1 * 3)

#Control statements

num = -5

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")

else:
    print("This number is negative")
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")) 

if num1 > num2:
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than" , num1) 
else:
    print("Both numbers are equal")
    
#Loops

fruits = ["apple", "banana", "cherry"] 

for fruit in fruits:
    print(fruit)  
    
numbers = [1, 2, 3, 5, 7] 

for number in numbers:
    print(number) 
    
#Using a while loop to count form 1 to 5    
count = 1

while count <= 5:
    print(count) 
    count += 1 # Increments the count by 1
    
#Loop Control Statements 

fruits = ["apple", "banana", "cherry", "date"]  
 
for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop if cherry is found
    print(fruit)

print() 

for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the next iteration
    print(fruit) 
    
print() 

for fruit in fruits:
    if fruit == "cherry":
       pass # Placeholder, no action is needed for cherry
    print(fruit) 
    
count = 0

while count < 5:
    print(count)  
    count += 1
    if count == 3:
        break #Exits the loop when the count is reached - 3                                  