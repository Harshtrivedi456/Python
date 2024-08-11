# Write a Python program to print all odd numbers between 1 to 100 using a while loop.
num=1
while num<101:
    if num%2!=0:
        print(num)
    num+=1

# Write a Python program to find the sum of all natural numbers between 1 to n.
num=1
sum=0
n=int(input('Enter the number'))
while num<n:
    sum=sum+num
    num+=1
print(sum)

# Write a Python function program to count a number of digits in a number.

# def count(num):
#     return
def count(number):
    num=str(number)
    return len(num)
    
num=int(input('Enter the integer'))
print(f"number of digits in ",{count(num)})

# Write a Python program to find the first and last digits of a number.

num=int(input('Enter the integer'))
num=str(num)
print('First didgit of your number is ',num[0])
print('Last digit of your number is ',num[-1])

# # Write a Python program to swap the first and last digits of a number.
def swapdigit(value):
    value_str = str(value)

    if len(value_str) ==1:
        return value
    
    first=value_str[0]
    last=value_str[-1]
    mid=value_str[1:-1]

    swapped_str=last+mid+first

    swapped=int(swapped_str)
    return swapped

value=int(input('Enter number'))
swapping=swapdigit(value)
print("Number after swapping digit is ",swapping)

def swap_first_last_digits(number):
    # Convert number to string to easily manipulate digits
    num_str = str(number)
    
    # Edge case: if the number has only one digit, return the number itself
    if len(num_str) == 1:
        return number
    
    # Swap first and last digits
    first_digit = num_str[0]
    last_digit = num_str[-1]
    middle_digits = num_str[1:-1]
    
    swapped_number_str = last_digit + middle_digits + first_digit
    
    # Convert back to integer
    swapped_number = int(swapped_number_str)
    
    return swapped_number

# Example usage:
number = 12345
print("Original number:", number)
swapped_number = swap_first_last_digits(number)
print("Number after swapping first and last digits:", swapped_number)

# Write a Python program to calculate the product of digits of a number.
n1=int(input('Enter the number'))
i=n1
pro=1
while (i !=0):
    pro=pro*(i%10)
    i=int(i/10)
print("Product of all digots is ",pro)




# Write a Python program to enter a number and print its reverse.

val=int(input('Enter the number'))
val=str(val)
print('Reverse order of your number: ',val[ ::-1])