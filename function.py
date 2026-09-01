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

def country(name="unknown"):
    print("country name is",name)
country("india")
country()
