# 1. If-Else Conditional Statements
# A) Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

'''
num = float(input("enter an integer: "))
print(num)
if(num>0):
    print("The number is positive!")

if(num<0):
    print("The number is negative!")

if(num == 0):
    print("The number is equal to zero!")
    
'''

#Create a program that checks if a person is eligible to vote (age >= 18).


'''
age = int(input("Enter your age: "))

if (age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
print("Sorry, try when you are 18")

'''

#Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
"""
number = int(input("enter a number:"))

if(number % 2 == 0):
    print("even")

else:
    print("odd")
 """   
    
#2. Match Case Statements
#Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
    
"""
day = int(input("enter a day number(1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
            print("friday")
    case 6:
            print("saturday")
    case 7:
            print("sunday")
    case _:
        print("ivalid day number")
        
    """
        
        
# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

"""
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))

op = input("enter an operation to be performed(+,-.*./) :")

match op:
    case "+":
        print("addition:", a+b)
    case "-":
        print("substraction:", a-b)
    case "*":
        print("multiplication:", a*b)
    case "/":
        print("division:", a/b)
    case _:
        print("Wrong operator!")
        
    """
    
#3. For Loops
# Print numbers from 1 to 10 using a for loop.
"""
i = 1

for i in range(1,11):
    print(i)
    
"""     
#Print the multiplication table of a number (entered by user).
"""
n = int(input("enter the number:"))

print("The table of",n,"is:")

for i in range(1,11):
    print(n, "X", i, "=", n*i)
    
"""
  #Calculate the sum of all numbers from 1 to 100 using a for loop.
""" 
i = 1
sum = 0
for i in range(1,101):
    sum+=i 
print(sum) 
            
"""

# Print the following pattern using a for loop:
# *
# **
# ***
# ****
'''
for i in range(1,5):
    print("*"*i)

'''


# 4. While Loops
# Print numbers from 1 to 10 using a while loop.
'''
i = 1
while (i <=10):
    print(i)
    i +=1
    
'''

#Write a program that keeps asking the user to enter a password until they enter the correct one.
'''
password = "aish"
entered_password = input("enter your password:")

while (entered_password != password):
    
    print("Wrong password.Try again")
    entered_password = input("enter your password:")
print("Successfully entered the correct password")
'''
#Use a while loop to reverse a given number (e.g., 123 → 321).
'''
num = int(input("enter the number:"))
print(str(num)[::-1]) 

'''
#Using "advanced slicing" to reverse a number in Python means using the extended slice syntax [::-1] on a string representation of that number. It quickly flips the digits backward by setting the step parameter to -1, without needing a loop.
'''
num = 70959
reverse_num = 0

while num > 0:
     # 1. Get the last digit
    digit = num % 10
     # 2. Add it to the reversed number
    reverse_num = (reverse_num *10) + digit
    # 3. Remove the last digit from the original number
    num = num // 10
    
print(reverse_num)
'''
#5. Break, Continue, and Pass Statements
# Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).

'''
i = 1
for i in range(1,11):
    if(i == 7):
        break
    print(i)
'''
# Print numbers from 1 to 10, skipping the number 5 (use continue).

'''
i = 1
for i in range(1,11):
    if(i == 5):
        continue
    print(i)
'''
#Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
i = 1
for i in range(1,6):
    if(i == 3):
        pass
    print(i)

    
