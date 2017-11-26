"Sorting hash tables"
import csv
def s(f="IDF.txt"):
    r=csv.reader(open(str("IDF.txt"),"r"))
    
    h={}
    f={}
    for i in r:
        h[i[0]]=i[1]
    i=0;
    w=csv.writer(open(str("IDF.txt"),"w"))
    for k in sorted(h.keys()):
        i+=1
        print i,"101 001"*i
        w.writerow([k,h[k]])
