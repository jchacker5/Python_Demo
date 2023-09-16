#this is a comment
#this is the second comment


print("Hello World")
#print has a default end of \n
print("Hello World", end="") #this is how to change the end of print
#line feed and carriage return are the same thing
print('-' * 40) #this is how to print a blank line
message: str = "this is a string" #this is a typehint
print(message)
# everything is an object in python

"this is also a comment, even though it is not a comment"

cap_message = message.capitalize() #this is how to capitalize a string
print(cap_message)

number: int = 23 #this is an int
print(type(number)) #this is how to get the type of the variable
print(number)

decimal = 5.8 #float is a clas in python 
print(type(decimal))

boolean = True #boolean is a class in python
print(type(boolean))
print(f'This is a  number: {34 + 6} and this is a string: {message}')

python_list = [1, 6.7, "joe", True,[45,7.8,"bob"],78] #this is a list with snake_case

str_element: str = python_list[2] #this is how to get an element from a list
print(str_element)
list_element: list = python_list[1:4] #this is how to get a slice of a list the ending index is not inclusive
print(list_element)

list_element = python_list[1:6:2] #this is how to get a slice of a list with a step
list_element = python_list[1:] #this is how to get a slice of a list with no end
list_element = python_list[:4] #this is how to get a slice of a list with no start
list_element = python_list[:] #this is how to get a slice of a list with no start and no end    
print(list_element)

list_element = python_list[4][1]  #this is how to get the last element of a list within a list

file_object = open("sample_names.txt") #this is how to open a file
print(type(file_object))