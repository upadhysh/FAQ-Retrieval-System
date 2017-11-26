import csv
import os
def match_1(a):
    re=csv.reader(open('FreqOfWords.txt','r'))
    a=a.lower()
    os.mkdir(a)
    for l in re:
        sub(l[0],a)
    #so()
    
   
def sub(a,b):
    sub_s=0
    p=0
    i=j=0
    la=len(a)
    lb=len(b)
    while j<lb:
        if(i==la):
            i=p
            j+=1
        elif a[i]==b[j]:
            #print a[i],' ',b[j]
            sub_s+=1
            p=i
            j+=1
        i+=1
    if sub_s>=2:
        sub_s=float(sub_s)
        f=str(b)+"\Match-LCS.txt"
        wr=csv.writer(open(f,"a"))
        if(la>lb):
            m=la
        else:
            m=lb
        m=float(m)
        f=float(sub_s/m)
        wr.writerow([a,f])
