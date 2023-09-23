from record_class import NameRecord #this is how to import a class from a file  
# #this is the second comment


# print('Hello World') #this is how to print to the console
# #print has a default end of \n
# print("Hello World", end="") #this is how to change the end of print
# #line feed and carriage return are the same thing
# print('-' * 40) #this is how to print a blank line
# message: str = "this is a string" #this is a typehint
# print(message)
# # everything is an object in python

# "this is also a comment, even though it is not a comment"

# cap_message = message.capitalize() #this is how to capitalize a string
# print(cap_message)

# number: int = 23 #this is an int not a primamitive data type in python
# print(type(number)) #this is how to get the type of the variable
# print(number)

# decimal = 5.8 #float is a clas in python 
# print(type(decimal))

# boolean = True #boolean is a class in python
# print(type(boolean))
# print(f'This is a  number: {34 + 6} and this is a string: {message}') #this is how to format a string

# python_list = [1, 6.7, "joe", True,[45,7.8,"bob"],78] #this is a list with snake_case

# str_element: str = python_list[2] #this is how to get an element from a list
# print(str_element)
# list_element: list = python_list[1:4] #this is how to get a slice of a list the ending index is not inclusive
# print(list_element)

# list_element = python_list[1:6:2] #this is how to get a slice of a list with a step. takes start, end, step
# list_element = python_list[1:] #this is how to get a slice of a list with no end
# list_element = python_list[:4] #this is how to get a slice of a list with no start
# list_element = python_list[:] #this is how to get a slice of a list with no start and no end    
# print(list_element)

# list_element = python_list[4][1]  #this is how to get the last element of a list within a list

file_object = open("sample_names.txt") #this is how to open a file
# print(type(file_object))

# first_line = file_object.readline() #this is how to read a line from a file
# print(first_line, end='') #this is how to read a line from a file and remove the line feed
# second_line = file_object.readline() #this is how to read a line from a file
# print(second_line)
# print(file_object.readline(), end='') #this is how to read a line from a file

# # this is how to use a for loop to read a file
# count = 0
# for line in file_object:
#     count += 1
#     print(f'{count} {line}', end='')
# file_object.close() #this is how to close a file

# for count, line in enumerate(file_object, 1): #this is how to use enumerate
#     print(f'{count} {line}', end='')

main_name_list = []
    
for line in file_object: #this is how to read all the lines in a file
    # name_dict = {
    #     'first_name': None,
    #     'last_name': None
    # } #this is how to create a dictionary with 2 keys
    
    split_line = line.split() #this is how to split a string
    
    name_record_obj = NameRecord(split_line[0], split_line[1]) #this is how to create an instance of a class
    
    # name_dict['first_name'] = split_line[0]
    # name_dict['last_name'] = split_line[1]
    # # print(name_dict) #this is how to print a dictionary
    # main_name_list.append(name_dict) #this is how to add an dicelement to a list
    print(main_name_list) #this is how to print a list
    
    for dict_obj in main_name_list:
        print(f"{dict_obj['first_name']} {dict_obj['last_name']}")