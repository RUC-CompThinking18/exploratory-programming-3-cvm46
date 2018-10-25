import re
infile = open('faust.txt', 'r')
text= infile.read()
def satanitcRegex(word):
    if type(word) != str:
        raise TypeError("EYY DUMBASS THIS AIN'T A STRING!")#this new york style error is necessary to show the user what they did wrong.
    matches =re.findall(r"\w*at\b",text)
    Jeffery=[]
    for word in matches:
        if len(word) > 3:
            Jeffery.append(word)
    print Jeffery#rather than returning the list just printing it will show us the results.
satanicRegex(text)#THIS IS NECESSARY FOR THE GODDAMN THING TO RUN! DO NOT FORGET IT! DO NOT!
