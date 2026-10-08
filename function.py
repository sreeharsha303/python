#FUNCTION :
#fuction are the block of code that prints set of statements when we call that fuction


'''def greet(): #creation fuction
    print("hello")
greet()#calling function

num1 = int(input("num1:"))
num2 = int(input("num2:"))

def subtract(a,b):
    return a-b

result = subtract(num1, num2)
print("output is ", result)'''


#arguments:
#Arguments are values that we pass to a function when calling it.
'''def greet (name):
    print("hello",name)
greet("harsha")

# multiple arguments  
def greet(name,location):
    print(f"hello",{name}and your from {location})
greet("harsha","bengalare")

num1 = int(input("enter the number1::"))
num2 = int(input("emter the number2::"))

def subtract(a,b):
    print("output is",a-b)
subtract(num1,num2)


#arguments types
#positional argument:Arguments are passed according to their position.
def greet(name,age):
    print(name)
    print(age)
greet("harsha",22)


#keyword argument: values are passed with the parameter name

def greet(name,location):
    print(name)
    print(location)
greet("harsha","pavagada")

#seqvence has to be maintained in keyword argument
#so we connot pass the values in any order'''

#default argument: we can assign default values to the parameters of a function. 
#If we do not pass any value to that parameter, then the default value will be used. 

'''def greet(name,location="pavagada"):
    print(name)
    print(location)

greet("harsha")'''

'''def country(name="unknown"):
    print("country name is",name)
country("india")
country()'''


#variable length argument: *args:
#this is used to take multiple arguments in a function.
#it is used when we do not know how many arguments will be passed to a function.
'''def greet(*names):
    for name in names:
        print("hello",name) 
greet("harsha","john","jane")'''

'''def sum(*args):
    print(args)
    print(type(args))
sum(10,20)
sum(10,20,30)
sum(10,20,30,40,50)'''


#num1 = int(input("enter the number1::"))
#num2 = int(input("enter the number2::"))    
'''def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(add(1,2,3,4,6,7,5))
print(add(10,20,30,40,50))'''


#variable length keyword argument: **kwargs:
#this is used to take multiple keyword arguments in a function. OR
#this is used to pass a variable number of keyword arguments to a function.






def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="harsha",age=22,location="pavagada")
my_function(name="john",age=25,location="bengaluru",country="india")



