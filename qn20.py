#20. Write a Python class to find the three elements that sum to zero
#from a list of n real numbers.
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]


def check(list_of_number):
    list_of_number.sort()
    lst = []
    for first in list_of_number:
        for second in list_of_number:
            for third in list_of_number:
                sum = first + second + third
                numbers = [first, second, third]
                if sum == 0:
                    numbers.sort()
                    if numbers not in lst:
                        lst.append(numbers)
    return lst
input_list=[-25, -10, -7, -3, 2, 4, 8, 10]
res = check(input_list)
print(res)