



text = open("tweets.txt").read()

lower_case = text.lower()

split_words = text.split("\n")



words = []
for word in split_words:
    words.append(word)

#print(words)



negative_words = open("negative_words.txt")#.read()

nw = []
for nwords in negative_words:
    nw.append(nwords)


#print(nw) 

p_words = open("positive_words.txt")#.read()   

pw = []
for pwords in p_words:
    pw.append(pwords)


print(pw)