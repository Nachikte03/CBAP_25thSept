# -*- coding: utf-8 -*-
# Reads a Number and Prints a Message If It Is Positive

number = int(input("Enter a number"))
if number >= 0:
    print(f"The number entered by user is a positive number")


# Program 3.2: Program to Read Luggage Weight and Charge the Tax Accordingly

weight = int(input("How many pounds does your suitcase weigh?"))
if weight > 50:
    print(f"There is a $25 surcharge for heavy luggage")
    print(f"Thank you")


# Program 3.3: Program to Find If a Given Number Is Odd or Even

number = int(input("Enter a number"))
if number % 2 == 0:
    print(f"{number} is Even number")
else:
    print(f"{number} is Odd number")


# Find the Greater of Two Numbers

number_1 = int(input("Enter the first number"))
number_2 = int(input("Enter the second number"))
if number_1 > number_2:
    print(str(number_1), " is greater than " , str(number_2))
else:
    print(f"{number_2} is greater than {number_1}")
    
    
    
# Prompt for a Score between 0.0 and 1.0. If the
# Score Is Out of Range, Print an Error. If the Score Is between 0.0
# and 1.0, Print a Grade Using the Following Table
# Score   Grade
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
# < 0.6    F

score = float(input("Enter your score"))
if score < 0 or score > 1:
    print('Wrong Input')
elif score >= 0.9:
    print('Your Grade is "A" ')
elif score >= 0.8:
    print('Your Grade is "B" ')
elif score >= 0.7:
    print('Your Grade is "C" ')
elif score >= 0.6:
    print('Your Grade is "D" ')
else:
    print('Your Grade is "F" ')


# Display the Cost of Each Type of Fruit

fruit_type = input("Enter the Fruit Type:")
if fruit_type == "Oranges":
    print('Oranges are $0.65 a pound')
elif fruit_type == "Apples":
    print('Apples are $0.38 a pound')
elif fruit_type == "Bananas":
    print('Bananas are $0.42 a pound')
elif fruit_type == "Cherries":
    print('Cherries are $2.00 a pound')
else:
    print(f'Sorry, we are out of {fruit_type}')
    
# Display First 10 Numbers Using
# while Loop Starting from 0

i = 0

while i < 10:
    print(f"Current value of i is {i}")
    i = i + 1


# Find the Average of n Natural Numbers



number = int(input("Enter a number up to which you want to find the average"))
i = 0
sum = 0
count = 0
while i < number:
    i = i + 1
    sum = sum + i
    count = count + 1
average = sum/count
print(f"The average of {number} natural numbers is {average}")



# Find the GCD of Two Positive Numbers

m = int(input("Enter first positive number"))
n = int(input("Enter second positive number"))

if m == 0 and n == 0:
    print("Invalid Input")

elif m == 0:
    print(f"GCD is {n}")

elif n == 0:
    print(f"GCD is {m}")

else:    
    while m != n:
        if m > n:
            m = m - n
        if n > m:
            n = n - m
            
    print(f"GCD of two numbers is {m}")




# Demonstrate Infinite while Loop and break

n = 0
while True:
    print(f"The latest value of n is {n}")
    n = n + 1
    if n > 15:
        print(f"The value of n is greater than 15")
        break



# Check Whether a Number Is Prime or Not

number = int(input('Enter a number > 1: '))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    

# Demonstrate continue Statement

n = 10
while n > 0:
    print(f"The current value of number is {n}")
    if n == 5:
        print(f"Breaking at {n}")
        n = 10
        continue
    n = n - 1













