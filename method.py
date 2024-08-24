message = 'python is fun'
# convert message to uppercase
print(message.upper())
message = input("Enter String")
# convert message to lowercase
print(message.lower())

text = 'CE Department'
replaced_text = text.replace('CE', input('Enter word:'))
print(replaced_text)

message = 'Python is a fun programming language'
# check the index of 'fun'

print(message.find(input('Enter word')))


title = 'Python Programming   '
result = title.rstrip()
print(result)

text = 'Python is fun'
# split the text from space
print(text.split())

message = 'Python is fun'
# check if the message starts with Python
print(message.startswith('Python'))

pin = "523"
# checks if every character of pin is numeric 
print(pin.isnumeric())

text = 'Python is fun'
# find the index of is
result = text.index('is')
print(result)

name = input('Enter the name ')
country = input('Enter country ')
print(f'{name} is from {country}')

str = "This is a \n normal string example" 
print(str) 
raw_str = r"This is a \n raw string example" 
print(raw_str)

