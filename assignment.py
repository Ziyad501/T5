



text = open("T5Projects/tweets.txt").read()

lower_case = text.lower()

split_words = text.split()



words = []
for word in split_words:
    words.append(word)

#print(words)



negative_words = open("T5Projects/negative_words.txt")

nw = []
for nwords in negative_words:
    nw.append(nwords)


#print(nw) 

p_words = open("T5Projects/positive_words.txt")    

pw = []
for pwords in p_words:
    pw.append(pwords)


print(pw)