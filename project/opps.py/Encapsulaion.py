'''
ENCAPSULATION : encapsulation means wrapping data (variables) and methods (functions) together inside a class 
and controlling access to that data

in simple words
encapsulation = data + methods + data protection

think like atm  : 
you can use the atm to withraw money but you cannot access the internal data of the atm machine


# ACCESS SPECIFIERS:
PUBLIC : public members are accessible from anywhere in the program
PRIVATE : private only we can access inside the class (used -- underscore _ before the variable name)
PROTECTED : protected con be accessed inside outer class

'''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__bal = balance  # private variable

    def get_balance(self):# used getter method
        return self.__bal

    def deposit(self, amount):# used setter method
        if amount > 0:
            self.__bal += amount
            print("Deposit successful")
        else:
            print("Invalid amount")


b1 = BankAccount("John", 1000)

print(b1.get_balance())

b1.deposit(500)

print(b1.get_balance())

#getter method is used to access the private variable  
#  setter method is used to modify the private variable


'''
ENCAPSULATION USING PROTECTED MEMBERS

protected member are accessible inside the class and its subclasses.

'''

class employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # protected variable
class manager(employee):
    def show_salary(self):
        print(self._salary)
m1 = manager("John", 50000)
m1.show_salary()  # accessing protected variable from subclass