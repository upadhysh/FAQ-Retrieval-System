import main
import re
import csv
import slangs

stop={}
st=csv.reader(open('Stop.txt','r'))
for i in st:
    stop[i[0]]=i[1]


def convert(li):
    val=10
    for x in range(len(li)-1,-1,-1):
        if li[x]==1:
            val+=val
    return val
        
def remStop(l):
    s=''
    for x in l.split(' '):
        try:
            if stop[x]:
                continue
        except:
            s+=x+' '
    return s.strip()


def lo(m,ques):
    qur=''
    maxo=int(0)
    lq=len(ques)
    for x in m:
        if(int(m[x])>maxo):
            maxo=int(m[x])
            qur=x
        elif maxo==int(m[x]):
            l1=len(x)
            l2=len(qur)
            if abs(lq-l1)<abs(lq-l2):
                qur=x
            elif abs(lq-l1)==abs(lq-l2):
                if l1<l2:
                    qur=x
    #print qur,maxo,'2'*10
    return maxo

def check(w,fi):
    #print 'in check'
    #r=csv.reader(open('Final/'+fi+'.txt','r'))
    for x in r:
        if x[0]==w:
           #print fi,w
           # print '******'
            return True
    return False


def prob(l,ques):
    ques=remStop(ques)
    #print ques
    #print 'in prob'
    m={}
    m2={}
    i=int(0)
    j=int(0)
    files=ques.split(' ')
    for x in files:
        if x == '':
            files.remove('')
        
    #print files
    #print l
    for x in l:
        m[x]=[]
    for x in l:
        j=0
        li=[0 for i in range(0,len(files))]
        x.strip()
        wo=x.split(' ')
        n=0
        for xc in wo:
            if xc == '':
                wo.remove('')
        #print wo  
        for fi in files:
            c=0
            for ind in range(0,len(wo)):
                w=wo[ind]
                #print w,fi
                if len(w)>0 and (w[0]==fi[0] or w[len(w)-1]==fi[len(fi)-1]):
                        if check(w,fi):
                            c=1
                            if c==1:
                                break
                
            if(c==1):
                li[n]=1
            n+=1

        m[x]=li
        #print x,m[x]
        #print'****'*9
    #print '*********************'
    for k,v in m.items():
        m2[k]=int(convert(v))
        #print k,v
        #print k,m2[k]
    #print '*********************'
    return m2
                


def read(msg):
    msg=msg.strip()
    msg=re.sub(r"[^a-zA-Z0-9\n%]",r" ",msg)
    msg=msg.lower()
    msg=slangs.removeSlangs(msg)
    print msg
    qpo=main.query(msg)
    h=prob(qpo.keys(),msg)
    maxo=lo(h,msg)
    end={}
    for k,val in qpo.items():
        end[k]=float(qpo[k]*h[k]/maxo)
        print k,end[k]
    max2=lo(end,msg)
    ans=[]
    for i in end.keys():
        if end[i]==max2:
            ans.append(i)
    print ans


if __name__=="__main__":
    print "enter question"
    msg=raw_input()
    msg=re.sub(r"[^a-zA-Z0-9\n%]",r" ",msg)
    msg=msg.lower()
    l=main.query(msg)
    #print l
    print prob(l,msg)


