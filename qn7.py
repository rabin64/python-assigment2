#7. Create a list of tuples of first name, last name, and age for your
#friends and colleagues. If you don't know the age, put in None.
#Calculate the average age, skipping over any None values. Print out
#each name, followed by old or young if they are above or below the average age.

friends_list = [('ram', 'Shrestha', 25), ('saroz', 'Poudel', None), ('rabin', 'shrestha', 22), ('rupace', 'pandit', 22),
                ]
sum_age = 0
count = 0
for items in friends_list:
    if items[2] != None:
        count += 1
        sum_age += items[2]
avg_age = sum_age // count

for items in friends_list:

    if items[2] != None:
        print(items[0], end=':-')
        if items[2] > avg_age:
            print('Old')
        else:
            print('Young')
