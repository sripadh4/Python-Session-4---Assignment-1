# Python-Session-4---Assignment-1
Function to filter list of words based on an integer and return a the list that meets the filter

def filter_long_words(a, b):
    a = input("Enter list of words separated by 'Space': ")
    b = input("Enter word threshold: ")
    d = list(filter(lambda c: len(c) > int(b), a.split(" ")))
    return (d)
