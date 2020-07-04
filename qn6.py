#6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

def find_John(name_list):
    for name in range(len(name_list)):
        N="john"

        if N in name_list:
            msg = "john found"
        elif N not in name_list:
            msg = "not found"
    return msg
name_list=[]
size=int(input("enter the number of friend list you want to enter:"))
for i in range(size):
    name=input("enter the friend name:")
    name_list.append(name)
print(name_list)
print(find_John(name_list))
