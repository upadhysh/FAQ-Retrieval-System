

import main
import csv


r=csv.reader(open('Stop.txt','r'))
s=''
for x in r:
    s=s+' '+x[0]
print main.query(s)
print s
