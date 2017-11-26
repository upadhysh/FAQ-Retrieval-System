import csv
import os
def match_2(a):
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
        f=str(b)+"\Match-SR.txt"
        wr=csv.writer(open(f,"a"))
        f=float(2*sub_s/(la+lb))
        wr.writerow([a,f])
