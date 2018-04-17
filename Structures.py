#Alinea Grace Del Mundo
#Structure


letters = ['a','l','i','n','e','a','g','r',
                'a','c','e','s','a','n','a','m',
                'a','k','a','p','a','s','a',
                's','a','l','a','h','a','t']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(5)
print ("letters repeated")
print(repeat)
