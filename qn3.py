#3. Write code that will print out the anagrams (words that use the same
#letters) from a paragraph of text.



def groupAnagrams(words):

	# sort each word in the list
    #A= words.sort()
    A = [''.join(sorted(word)) for word in words]
    # construct a dictionary where key is each sorted word
    # and value is list of indices where it is present
    dict = {}
    for i, e in enumerate(A):
        dict.setdefault(e, []).append(i)

	# traverse the dictionary and read indices for each sorted key.
	# The anagrams are present in actual list at those indices
    for index in dict.values():
        print([words[i] for i in index])

if __name__ == '__main__':
    str = input("enter a string:")
    words = str.split()
    groupAnagrams(words)