# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing dictionary elements
print(my_dict['name'])  # Output: John

# Updating dictionary elements
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Adding new key-value pairs
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}

# Removing key-value pairs
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

# Checking if a key exists
if 'name' in my_dict:
    print('Name exists in the dictionary')

# Getting the number of key-value pairs
print(len(my_dict))  # Output: 3

# Getting a list of all keys
print(my_dict.keys())  # Output: ['name', 'age', 'occupation']

# Getting a list of all values
print(my_dict.values())  # Output: ['John', 26, 'Engineer']

# Getting a list of all key-value pairs
print(my_dict.items())  # Output: [('name', 'John'), ('age', 26), ('occupation', 'Engineer')]

# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}
# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing dictionary elements
print(my_dict['name'])  # Output: John

# Updating dictionary elements
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Adding new key-value pairs
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}

# Removing key-value pairs
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

# Checking if a key exists
if 'name' in my_dict:
    print('Name exists in the dictionary')

# Getting the number of key-value pairs
print(len(my_dict))  # Output: 3

# Getting a list of all keys
print(my_dict.keys())  # Output: ['name', 'age', 'occupation']

# Getting a list of all values
print(my_dict.values())  # Output: ['John', 26, 'Engineer']

# Getting a list of all key-value pairs
print(my_dict.items())  # Output: [('name', 'John'), ('age', 26), ('occupation', 'Engineer')]

# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}
