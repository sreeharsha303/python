#A dictionary in Python is a built-in data type used to store data in key-value pairs. It is mutable (can be changed), unordered , and keys must be unique.

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student)

student["city"] = "New York"   # Add a new key-value pair
student["age"] = 21            # Update an existing value

print(student)

student.pop("grade")   # Removes the key 'grade'
print(student)

# update method : used to update the  key value pair in th dictionary
student.update({"email":"shreeharha303@gmail.com"})


#Advantages of Dictionaries
#Store data as key-value pairs for easy lookup.
#Fast access to values using keys.
#Can store different data types.
#Mutable, allowing easy updates and modifications.

#A dictionary is ideal when you need to associate a unique key (such as a name, ID, or product code) with a corresponding value.,,,

# methods 
# keys : keys are used to access the keys
print(student.keys())

# values : values are used to access the values
print(student.values())

# items : items are used to access both keys and values
print(student.items())
