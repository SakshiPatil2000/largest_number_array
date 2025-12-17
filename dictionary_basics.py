# create empty dictionary
empt_dict ={}
print(empt_dict)

# example

employee ={
    'name':'Sakshi',
    'role':'Junior Mobile Developer',
    'age':25,
    'salary':4.6
}

print(employee)
print(employee['age'])
print(employee['name'])
print(employee['role'])
print(employee['salary'])
employee['name']='Sakshi Patil'
print(employee)
employee['address']='Pune'
print(employee)

# Nested dictionary

student ={
    'name' : 'Sakshi',
    'age' :25,
    'email' : 'sakshi@screem-magic.com',
    'role':{
        'frontend':'Flutter',
        'backend' : 'Python'
    }
}

print(student)
print(student['name'])
print(student['role'])

print(student['role']['frontend'])


# Methods in dictionary 

print(student.keys())  # returns all 
print(list(student.keys())) #returns list
print(student.values()) #retruns all values
print(student.items()) # returns all key value pair as tuple
print(student.get('name')) #returns value if key is there or returns none if no key found
print(student['name'])  #returns error if no key found
student.update({'mobile_no':8888888888}) # used to add new key value pair to dictionary
print(student)


#create a dictionary by taking user input 

marks ={}

x=int(input("Enter marks of physics : "))

marks.update({'physics':x})

y=int(input("Enter marks of maths :"))

marks.update({'maths':y})

z=int(input("Enter marks of chemistry :"))

marks.update({'chemistry':z})

print('Updated marks disctionary is :\n',marks)