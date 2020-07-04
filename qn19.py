#19. Write a Python class to find validity of a string of parentheses, '(',
#')', '{', '}', '[' and ']. These brackets must be close in the correct order,
#for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def check(mystring):
    lst = []
    for i in mystring:
        if i in open_list:
            lst.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(lst) > 0) and (open_list[pos] == lst[len(lst) - 1])):
                lst.pop()
            else:
                return "incorrect order"
    if len(lst) == 0:
        return "correct order"
    else:
        return "incorrect order"


mystring=input("enter a paranthesis cobinatio to check:")
print(mystring, "-", check(mystring))


