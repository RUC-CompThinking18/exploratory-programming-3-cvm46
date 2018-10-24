import re
infile = open('faust.txt', 'r')
text= infile.read()
def satanitcRegex(word):
    if type(word) != str:
        raise TypeError("EYY DUMBASS THIS AIN'T A STRING!")
    matches =re.findall(r"\w*at\b",text)
    Jeffery=[]
    for word in matches:
        if len(word) > 3:
            Jeffery.append(word)
    print Jeffery
satanicRegex(text)
