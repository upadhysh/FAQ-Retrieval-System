import main
import re
import csv
def lo(m):
    l=sorted(m,reverse=True)
    return m

def check(w,fi):
    #print 'in check'
    r=csv.reader(open('c:/Python27/Final/'+fi+'.txt','r'))
    for x in r:
        if x[0]==w:
            print '******'
            return 1
    return 0

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
        p=int(0)
        c=int(0)
        for i in range(p,len(files)):
            fi=files[i]
            for j in range(0,len(wo)):
                w=wo[j]
                lw=len(w)-1
                lf=len(fi)-1
                print w,fi
                if(w[0]==fi[0] or w[lw]==fi[lf]):
                    print w,fi
                    c=int(check(w,fi))
                    if c==1:
                        m[x]+=1
                        p=i+1
                        break
        print x,m[x]
        #except:
         #   print '***',x,m[x]
    #return lo(m)
                

'''
if __name__=="__main__":
    print "enter question"
    msg=raw_input()
    msg=re.sub(r"[^a-zA-Z0-9\n%]",r" ",msg)
    msg=msg.lower()
    l=main.query(msg)
    print l
    print prob(l,msg)
'''
