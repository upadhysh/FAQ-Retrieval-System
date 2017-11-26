import re
import csv
def prob():
    f=open("big.txt","r")
    s=''
    for i in f:
        s+=i
    s=s.lower()
    s=re.sub(r'[^a-zA-Z0-9]',r' ',s)
    #w=open('test.txt','w')
    #w.write(s)
    h={}
    l=s.split()
    for i in l:
        try :
            h[i]+=1
        except:
            h[i]=1
    wr=csv.writer(open("prob.txt","w"))
    k=sorted(h.keys())
    maxi=h[k[0]]
    #print maxi,"pp"
    for i in k:
        if h[i]>maxi:
            #print h[i],"*",maxi
            maxi=h[i]
        wr.writerow([i,h[i]])
    #w.close()
    print maxi
