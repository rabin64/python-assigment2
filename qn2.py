#2. Write an if statement to determine whether a variable holding a year is a leap year.

leap_year = int(input("enter a four digit leap year:"))

def leap(leap_year):
    if (leap_year%4==0 or leap_year%400 ==0 )and leap_year%100 != 0 :
        return print("valid leap_year")
    else:
        return print("invlid one")

leap(leap_year)