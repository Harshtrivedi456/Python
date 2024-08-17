
list1=[1,2,11,2,3,4,4,5]
# print(list(dict.fromkeys(list1))) 
list2=[1,2,3,4,5]
print(set(list1)&set(list2))
print(list(zip(list1,list2)))


list_of_lists = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]
# using list comprehension
my_list = [item for List in list_of_lists for item in List]
print(my_list)

list1=[1,2,11,2,3,4,4,5]
print(list1.index(4,3,7))

