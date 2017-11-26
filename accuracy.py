
import main
import re
import csv

r=csv.reader(open('test.txt','r'))
total=int(0)
x1=int(0)
accu=int(0)
testcases=int(0)
hit=int(0)
for i in r:
    #print i[0]
    s=i[0].lower()
    s=re.sub(r'[^a-zA-Z0-9]',r' ',s)
    r=i[1].lower()
    r=re.sub(r'[^a-zA-Z0-9]',r' ',r)
    l=main.query(s)
    testcases+=1
    #print l,'\n'
    for x in l:
        #print x
        if str.strip(x)==str.strip(r):
            hit+=1
            #print x,'\n',x1
            print '************\n'
            break
        else :
            x1+=int(1)
    #print "#################################################\n"
    accu+=int(x1)
    total+=int(10)
    #print accu,total,x1,'\n',l,'\n',s,'\n',r
    x1=0
print "Accuracy (in terms of number of questions able to correct)=\t",int (100*hit/testcases)
print 'Accuracy is (in terms of position in q-poss) =\t',int(100-100*accu/total),'\n',accu,total
