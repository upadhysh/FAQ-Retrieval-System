import csv
import re

def  removeSlangs(l):
    re=csv.reader(open('sl.txt','r'))
    li=l.split()
    h={}
    for x in re:
        h[x[0]]=x[1]
       # print x[0],x[1]
    tampered=''
    for a in li:
        try:
            tampered+=h[a].strip()+' '
        except:
            tampered+=a+' '
    return tampered.strip()
