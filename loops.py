#loops : are used to do a particular task repeatedly until a certain condition is met. 
# There are two types of loops in python : for loop and while loop.

#while loop : this loop print a particular black of statements repeatedly until the given condition is true.

'''i = 1
while i <= 5:
    print("hello world")
    i += 1'''


# to print 1 to 10 number
'''i = 1
while i <= 10:
    print(i)
    i += 1
print("executed completed")'''

# to print 10 to 1 number
'''i = 10
while i >= 1:
    print(i)
    i -= 1
print("executed completed")'''

#take number from users and print it multiplication table
'''num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1'''


#print the even numbers
'''num = int(input("Enter the number"))
i = 0
while i <=10:
  #if i % 2 == 0:   this method also used to print even numbers  
    print(i)
    i += 2'''

#prnt the odd numbers
'''num = int(input("Enter the number"))
i = 1
while i <= 10:
    print(i)
    i += 2'''

#for loop : is used to acccess the items from an iterable object like list, tuple, string etc. 

 #while loop : user does not know where to stop the loop
 #for loop : user knows where to stop the loop
#for i in range(1, 11):
    #print(i)

#print the even numbers using for loop
'''num = int(input("Enter the number: "))
for i in range(0, num+1, 2):
    print(i)

#print the odd numbers using for loop
num = int(input("Enter the number: "))
for i in range(1, num+1, 2):
    print(i)'''








#print multiplication table using for loop
'''num = int(input("Enter the number:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i) '''
#for loop in itterable objects
#access items of a list using for loop
'''fruits = ["apple", "banana", "cherry","watermelon"]
for i in fruits:
    print(i,end="")'''
#access items of a tuple using for loop
'''fruits = ("apple", "banana", "cherry","watermelon")
for i in fruits:
    print(i,end="")'''

#access items of a dictionary using for loop
'''student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)'''

#list1 = ["apple","banana","cherry"]
#list2 = ["red","yellow"]
for j in range(5):
    for i in range(5):
        print("*", end=" ")
    print()
