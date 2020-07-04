#Create a list. Append the names of your colleagues and friends to it.
#Has the id of the list changed? Sort the list. What is the first item on
#the list? What is the second item on the list?

lst = []
size=int(input("enter the number of friend list you want to add:"))

for items in range(size):
    name=input("enter the name:")
    lst.append(name)

print(lst)

lst.sort()
#A=[''.join (sorted(word)) for word in lst]

print(lst)


print(f'first item {lst[0]} and second item {lst[1]}')

