import pickle
"Loading Questions and calculating frequency of each word"

ha={}
li=pickle.load(open("AllQues.txt","r"))
for i in li:
    j=i.split()
    for a in j:
        if a in ha.keys():
            ha[a]+=1
        else:
            ha[a]=1
"Frequency of each word is stored in a hash table"

import csv
w=csv.writer(open("FreqOfWords.txt","w"))

l=sorted(ha.keys())
for key in l:
    w.writerow([key,ha[key]])
            
