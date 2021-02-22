def sort_words(string):
    words = string.split()
    """
    append lowercase and copy using list comprehension 
    """
    words = [w.lower() + w for w in words]
    """
    sort string using sort function
    """
    words.sort()
    """
    assemble the rest of list by string separated by space 
    """
    words = [w[len(w)//2:] for w in words]

string = "banana ORANGE apple"
print(sort_words(string))

