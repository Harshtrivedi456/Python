# l=[1,2,3,4,5]
# n=1
# for i in l:
#   n=n*i
# print(n)

# L=[12,445,43,56,76,4323,455,3]
# print('Largest number is: ',max(L))

# LI1=[1,23,23,34,43,43,45,55,56,54]
# print('List without duplicate is ',list(dict.fromkeys(LI1)))

# list = [1,2,2,1,3,4,1,2,2,1,4,5,3]
# element= max(set(list), key=list.count)
# print("frequency of elements in a list is = ", element)

N=[12,1,23,34,45,55,56]
M=[32,23,1,12,55,56]
s=list[set(N)&set(M)]
print(s)

list1=[1,2,3,3,2,1,1]
h=0
for i in list1:
    h=(h*10)+i
print(h)