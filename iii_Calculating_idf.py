
"Counting Number of Questions"
import pickle
r=pickle.load(open("AllQues.txt","r"))
l=float(len(r))

"CAlculating IDF and storing in hash table"
import math
import csv
h={}
r=csv.reader(open("FreqOfWords.txt","r"))
for i in r:
    try:
        h[i[0]]=float(math.log(l/int(i[1]))/math.log(10))
    except:
        print i[0]," ",i[1]        
"Creating New File for IDF"
wr=csv.writer(open("IDF.txt","w"))

l=sorted(h.keys())
for key in l:
    wr.writerow([str(key),h[key]])
            
