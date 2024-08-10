# Write a Python program to Count the occurrences of an element in a tuple.
tup=(1,2,3,3,2,1,4,4,5,6,7)
print('Element 3 is occurre ',tup.count(3),'time')

# Write a Python program to Check if an element exists in a tuple.
tup1=(1,2,3,4,5,6,7)
print(tup1.count(8))

# Write a Python program to Convert a tuple to a string.
tup2=(1,2,3,4,5)
n=0
for i in tup2:
    n=(n*10)+i
print(n)

# Write a Python program to Find the maximum and minimum elements in a tuple.
tup3=(1,2,3,44,5,6,77,789,9)
print('Maximum number from tup3 is ',max(tup3))

# Write a Python program to convert a tuple of strings to a single string.
tup4=('apple','mango','guava','orange')
str="".join(tup4)
print(str)

# Write a Python program to sort a tuple of integers.
tup5=(1,3,4,5,2,3,5,6,7,8,5)
# print(tup5.sort())
li=tuple(sorted(tup5))
print(li)

# Write a python program to find the first and last elements of a tuple.
tup6=(1,2,3,4,5,6)
print('First element of the tup`le is ',tup6[0])
print('Last element of the tuple is ',tup6[-1])