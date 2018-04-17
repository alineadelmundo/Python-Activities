#Alinea Grace M. Del Mundo
#Cpe Petition
#Data Structure


def only_upper(s):
    upper_chars = ("A gOod Man is HARd To Find")
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

only_upper(s)
