import csv
import re

r=open('Nslang.txt','r')
wr=csv.writer(open('sl.txt','w'))
h={}
for i in r:
    c=i.split('-')
    h[c[0].strip()]=c[1].strip()
l=sorted(h.keys())
for k in l:
    x=re.sub(r'[^a-zA-Z0-9]',' ',h[k])
    wr.writerow([k.lower(),x.lower()])




