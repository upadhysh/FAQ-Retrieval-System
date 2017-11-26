import pickle
import csv
import math
import re
import os
import slangs

stop={}
st=csv.reader(open('Stop.txt','r'))
for i in st:
    stop[i[0]]=i[1]
try:
    os.mkdir("c:/Python27/Final",0777)
except:
    poiu=90

def remStop(l):
    w=l.split()
    s=''
    for i in w:
        try:
            if stop[i]:
                continue
        except:
            s+=i+' '
    return s


def len_stop(q):
    l=q.split(' ')
    i=0
    for x in l:
        try:
            if stop[i]==True:
                continue
        except:
            i+=1
    return i

def len_space(q):
    l=q.split(' ')
    i=0
    for x in l:
        i=i+len(x)
    return i
    


def lcsf(a,b):
    #print 'in lcsf'
    la=len(a)
    lb=len(b)

    l=[[0 for i in range(0,la+1)]for i in range(0,lb+1)]
    for i in range(1,lb+1):
        for j in range(1,la+1):
            if(a[j-1]==b[i-1]):
                l[i][j]=l[i-1][j-1]+1
            else:
                if l[i][j-1]>=l[i-1][j]:
                    l[i][j]=l[i][j-1]

                else: 
                    l[i][j]=l[i-1][j]
    return l[lb][la]



def weight(x):
    #print 'in weight'
    m=len(x)
    l={}
    ht={}
    fl=str(x) + ".txt"
    
    l=csv.reader(open('IDF.txt','r'))
    for k in l:
        w=k[0]
        if w[0]==x[0] or w[len(w)-1]==x[len(x)-1]:
            qwerty=0
        else :
            continue
        y=k[0]
        n=len(y)
        lcs=float(lcsf(x,y))
        if m>=n:
            maxx=m
        else:
            maxx=n
        
        zzz=float(lcs)/float(maxx)           #threshold
        smr=float((2*lcs)/float((m+n)))
        ld=maxx-lcs
        if zzz>0.3 and ld!=0:
            idf=float(k[1])
            lcsr=float(lcs)/float(maxx)
            z=smr*idf
            wght=(float(lcsr)*z)/float(ld)
            ht[y]=wght
            #print y,wght
        elif ld==0 :
            idf=float(k[1])
            wght=idf/.5
            ht[y]=wght
            #print y,wght
    nht={}
    for key,val in ht.items():
        if(val in nht.keys()):
            nht[val].append(key)
        else:
            nht[val]=[]
            nht[val].append(key)

    svht={}
    vli=[]
    vli=nht.keys()
    vli=sorted(nht.keys(),reverse=True)
    c=0
    new=csv.writer(open('c:/Python27/Final/'+fl,'w'))
    ind=0
    
    for kk in vli:
        for i in nht[kk]:
            if (len(i)>=int(len(x)*.70)and int(lcsf(x,i))>int (.70*len(x))):
                new.writerow([i,kk])

def posy(word,qposs,lenq):
    #print 'in posy'
    re=csv.reader(open('c:/Python27/Final/'+word+'.txt','r'))
    for  i in re:
        len_v=len(i[0])
        word=i[0]
        for k in qposs.keys():
            s=k.encode('UTF-8')
            l=s.split(' ')
            for w in l:
                if(len(w)==len_v and w[0]==word[0] and w[len_v-1]==word[len_v-1] and w==word):
                    qposs[k]+=(float(i[1])*len_v/float(len(k)))
                    break
            
    return qposs

def qpos10(ques,qposs):
    #print ques
    #print 'Questions'
    h={}
    for k in qposs.keys():
        try:
            h[qposs[k]].append(k)
        except:
            h[qposs[k]]=[]
            h[qposs[k]].append(k)
    l=sorted(h.keys(),reverse=True)
    ind=0
    #print h
    qtion={}
    for i in l:
        #print i,h[i]
        for q in h[i]:
            #print q,h[i]
            qtion[q]=i
            #print q,i
            #print '\n****************************\n'
            ind+=1
            if(ind>=25):
               # print '\n****************************\n'
                return qtion


def query(l):
    l=slangs.removeSlangs(l)
    #print l
    #print 'in query'
    lenq=0
    qposs={}
    msg=re.sub(r"[^a-zA-Z0-9\n%]",r" ",l)
    msg=msg.lower()
    msg=remStop(msg)
    print msg
    r=pickle.load(open('AllQues.txt','r'))
    for k in r:
        if (len_space(k)<float(4*len(l)) and len_space(k)>float(.75*len(l))):
            qposs[k]=float(0)
    token=[]
    for i in msg.split():
        lenq+=len(i)
        try:
            if stop[i]==True:
                qposs=posy(i,qposs,lenq)
                continue
        except:
            token.append(i)
    #print token
    for i in token:
        try:
            s='c:/Python27/final/'+str(i)+'.txt'
            p=open(s,'r')
            qposs=posy(i,qposs,lenq)
            continue
        except:
            #print i
            weight(i)
            qposs=posy(i,qposs,lenq)
    #print '\n#########################\n'
    #print qposs['he country that accounts for nearly one third of the total teak production of the world']
    return qpos10(msg,qposs)
 
    
