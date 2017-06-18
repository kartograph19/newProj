import operator 
text = input("Enter a string to be coded: ")
sequnceToCode = {x:round(text.count(x)/len(text),5) for x in set(text)}
s = sorted(sequnceToCode.items(),key = operator.itemgetter(1),reverse = True)


print(dict(s))



