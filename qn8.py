#Write a function, is_prime, that takes an integer and returns True if
#the number is prime and False if the number is not prime.

def is_prime(val):
    if val <= 1:
        return "False"
    for i in range(2,val):
        if val % i == 0:
            return "false"
    return "True"

number=int(input("enter a number:"))
print(is_prime(number))
