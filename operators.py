# arthmetic operators

a = 10
b = 5

print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus
print(a**b) #exponentiation
print(a//b) #floor division

#comparison operators : are uesed to compare two values and return a boolean result (True or False).
num1 = 10
num2 = 5
print(num1 == num2) #equal to
print(num1 != num2) #not equal to
print(num1 > num2) #greater than
print(num1 < num2) #less than
print(num1 >= num2) #greater than or equal to
print(num1 <= num2) #less than or equal to

#logical operators : are used to combine conditional statements and return a boolean result (True or False).

# and operator : returns True if both conditions are True
num1 = 10
num2 = 5
print(num1 > 5 and num2 < 10) #True
print(num1 > 5 and num2 > 10) #False

#or operator : returns True if at least one condition is True
num1 = 10
num2 = 5  
print(num1 > 5 or num2 < 10) #True
print(num1 > 5 or num2 > 10) #True
print(num1 < 5 or num2 > 10) #False 

#not operator : returns True if the condition is False and returns False if the condition is True
# this operator takes one condition and reverses the outputS
num1 = 10
num2 = 5        
print(not(num1 > 5)) #False
print(not(num2 < 10)) #False
print(not(num1 < 5)) #True 


#assignment operators : are used to assign or update the value of a variable
x = 10
print(x) #10
x += 2 # equivalent to x = x + 2
print(x) #12
x -= 2 # equivalent to x = x - 2
print(x) #10
x *= 5 # equivalent to x = x * 5
print(x) #50
x /= 5 # equivalent to x = x / 5
print(x) #10
x %= 5 # equivalent to x = x % 5
print(x) #0
x **= 5 # equivalent to x = x ** 5
print(x) #0
x //= 5 # equivalent to x = x // 5
print(x) #0   

#bitwise operators : are usd to perform operations on the individual bits of binary numbers

#and operator : it takes two numbers converts it int binary code  it gives 1 if both bits are 1 otherwise it gives 0
a = 10  # 1010 in binary
b = 5   # 0101 in binary
c = a & b  # 0000 in binary
print(c)  # 0

#or operator : it takes two numbers converts it int binary code  it gives 1 if at least one bit is 1 otherwise it gives 0
a = 10  # 1010 in binary    
b = 5   # 0101 in binary
c = a | b  # 1111 in binary
print(c)  # 15


#identity operators : are used to compare the memory location of two objects
 #num1 = [1, 2, 3]
 #num2 = [1, 2, 3]
 #num3 = num1
#print(num1 is num2) #False
#print(num1 is num3) #True
#print(num1 is not num2) #True
#print(num1 is not num3) #False
#print(id(num1)) #140706091234560
#print(id(num2)) #140706091234624
#Sprint(id(num3)) #140706091234560

#membership operators : are used to test if a value is present in a sequence (such as a list, tuple, or string)
num1 = [1, 2, 3, 4, 5]
print(3 in  num1) #True
print(6 in num1) #False
print(3 not in num1) #False
print(6 not in num1) #True


#in : returns True if the value is present in the sequence, otherwise returns False
#not in : returns True if the value is not present in the sequence, otherwise returns False