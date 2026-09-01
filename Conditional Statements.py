#Conditional Statements : is take the decision based on the condition. If the condition is true then it will execute the block of code otherwise it will not execute the block of code.
# if statement : is used to execute a block of code if the condition is true
#The if statement executes code only when the condition is True.

'''age = 18
age = int(input("Enter your age: "))
if (age >= 18):
    print("You are eligible to vote.")
elif (age < 18):
    print("You are not eligible to vote.")'''

#else statement : is used to execute a block of code if the condition is false
'''valid_age = 18
user_age = int(input("Enter your age: "))
if valid_age <= user_age:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")'''

'''gender = input("Enter your gender : ")
real_gender = gender.lower()
if gender == "male":
    print("You are a male.")
elif gender == "female":
    print("You are a female.")'''


#elif statement : is used to give multiple conditions to check.
#  It is used when we have more than two conditions to check.
'''gender = input("Enter your gender : ")
if gender == "male":
    print("You are a male.")
elif gender == "female":
    print("You are a female.")
else:
    print("please give a proper gender")'''

#program to find highest number
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1>num2 and num1>num3:
    print("num1 is greater than num2 and num3")
elif num2>num1 and num2>num3:
    print("num2 is greater than num1 and num3") 
else:
    print("num3 is greater than num1 and num2")




#nested if statement : if conditin  will be checked inside another if condition
'''user_age = 20
valid_id = True
if user_age >= 18:
    if valid_id:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")'''








'''num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1>num2 and num1>num3:
    print("num1 is greater than num2 and num3")
elif num2>num1 and num2>num3:
    print("num2 is greater than num1 and num3")
else:
    print("num3 is greater than num1 and num2")'''