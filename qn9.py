#9. Write a binary search function. It should take a sorted sequence and
#the item it is looking for. It should return the index of the item if found.
#It should return -1 if the item is not found.

def binary_search(items, value):
    flag = 0
    position = None
    for i in range(len(items)):
        if value == items[i]:
            flag = 1
            position = i

    if flag == 1:
        return position
    else:
        return -1

value=int(input("enter the item to be serached:"))
result = binary_search(sorted([1,2,4,5,8,7,6,3,9,10]), value)
print("index of the item:", result)