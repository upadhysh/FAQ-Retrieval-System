import main
import re
import csv

def check(w,fi):
    #print 'in check'
    r=csv.reader(open('c:/Python27/Final/'+fi+'.txt','r'))
    for x in r:
        if x[0]==w:
            print fi,w
            print '******'
            return True
    return False


def prob(l,ques):
    #print 'in prob'
    m={}
    i=int(0)
    j=int(0)
    #print l
    for x in l:
        m[x]=int(0)
    for x in l:
        files=ques.split(' ')
        j=0
        wo=x.split(' ')
        p=0
        for fi in files:
            p=j
            while p <len(wo):
                w=wo[p]
                try:
                    if(w[0]==fi[0] or w[len(w)-1]==fi[len(fi)-1]):
                        if check(w,fi):
                            m[x]=m[x]*10+p+1
                            j=p+1
                except:
                    print "BEwafa"
                finally:
                    p+=1
                        
        print x,m[x]
        print'****'*9
    
