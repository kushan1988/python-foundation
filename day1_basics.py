#Assigning String
name = "Ankush"
#Integer
roll_number = 0o1
#Float
total_score = 99.9
#Boolean
is_active = True

print(type(name)," ", type(roll_number)," ", type(total_score)," ", type(is_active))

print(f"My name is {name}")
#using f-Strings (allows embedding python expressions directly inside string literals)
print("My name is",name)

#Accept user input (Always return string)
number = input("Any number: ") 
print(f"Entered Number, {number}")

#check if number is even
if int(number) % 2 != 0:
    print(f"{number} is not even!")

else:
    print(f"{number} is even!")

#check if age is permitted
age = input("Enter your age: ")
permitted_age = 18
if int(age) >= permitted_age:
    print(f"Can cast Vote!")
else:
    print("Not permitted to cast vote!")

#compare two numbers
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
if int(first_number) > int(second_number):
    print(f"{first_number} is greater!")
elif int(second_number) > int(first_number):
    print(f"{second_number} is greater!")
else :
    print("Both are equal!")

#Celsius to Fahrenheit conversion
temp_C = input("Enter temperature in Celsius: ")
conversion_formula = (int(temp_C) * 9/5) + 32
print(f"Temperature in Fahrenheit is {conversion_formula}")

#Calculate Simple Interest
principal = input("Enter principal amount: ")
rate = input("Rate of interest: ")
time = input("Time Duration: ")
simple_interest = (int(principal) * int(rate) * int(time)) / 100
print(f"Calculated Simple Interest: {simple_interest}")

#Calculator
input_1 = input("Enter first number: ")
operator = input("Enter Operation (+,-,/,*)")
input_2 = input("Enter second number: ")
if input_2 == '0':
    result = 0
elif operator == '+':
    result = int(input_1) + int(input_2)
elif operator == '-':
    result = int(input_1) - int(input_2)
elif operator == '/':
    result = int(input_1) / int(input_2)  
elif operator == '*':
    result = int(input_1) * int(input_2)  
else:
    print("Invalid Operator! Try Again")
print(f"{result}")

