#10. Write a function that takes camel-cased strings (i.e.
#ThisIsCamelCased), and converts them to snake case (i.e.
#this_is_camel_cased). Modify the function by adding an argument,
#separator, so it will also convert to the kebab case
#(i.e.this-is-camel-case) as well.
def case_converter(camelcase):
    seperator='_'
    string = camelcase[0].lower()
    for letter in camelcase[1:]:
        if letter.isupper():
            string += seperator + letter.lower()
        else:
           string += letter
    return string

res = case_converter('MyNameIsRabinShrestha')
print("snake case:", res)

def case_converter(camelcase, seperator):
    string = camelcase[0].lower()
    for letter in camelcase[1:]:
        if letter.isupper():
            string += seperator + letter.lower()
        else:
           string += letter
    return string

res = case_converter('MyNameIsRabinShrestha', '-')
print("kebab case:", res)