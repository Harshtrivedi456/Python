string4 = 'ICT Department'
# access character from 1st index to 3rd index
print(string4[1:4])  
print(string4[:2])
print(string4[2:])

#STRINGS ARE IMMUTABLE
message = 'ICT Department'
message[0] = 'H'
print(message)

message = 'ICT'
print(message)
# assign new string to message variable
message = input('Enter new String: ')
print(message)

#Python Multiline String
message = """
ICT
Department
3EK1
"""
print(message)

#1. Compare Two Strings
str1 = "ICT"
str2 = "Department"
str3 = "3EK1"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

#2. Join Two or More Strings
greet = "ICT"
name = "Department"
# using + operator
result = greet + name
print(result)

#Python String Length
greet = input('ENTER THE STRING: ')
print(len(greet))

#String Membership Test
Str=input('Enter the String: ')
letter=input('Enter which letter you want to find: ')
print(letter in Str) 
print('at' not in Str) 
