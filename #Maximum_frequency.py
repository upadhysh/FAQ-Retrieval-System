import csv
r=csv.reader(open("FreqOfWords.txt","r"))
maxi=0
for i in r:
    if(i[1]>maxi):
        maxi=i[1]
print maxi
