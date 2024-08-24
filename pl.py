#length of the string
str=input('Enter the String')
print(str[::-1])


#Write a Python program to check if a string is a palindrome.
str1=int(input('Enter number: '))
str2=str(str1)[ ::-1]
if str(str1)==str2:
    {
        print('Number is palindrome')
    }
else:
    {
        print("""Number isn't palindrome""")
    }

#Write a Python program to check if a string contains only digits.
str='45ASD5'
print(str.isnumeric())

#Write a Python program to find the longest word in a sentence.
str1='PYTHON programming is fun'
# list=str(str1.split())
str2=str(str1[7:18])
print(str2)
print(len(str2))









#Write a Python program to find the length of the last word in a sentence.
str1='Programming with python'
str2=len(str1[-6:-1])
print('Length of the longest number is ',str2)

