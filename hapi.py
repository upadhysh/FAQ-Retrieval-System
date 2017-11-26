import pickle
import csv
import math
import re
import os

def lcsf(a,b):
    la=len(a)
    lb=len(b)

    l=[[0 for i in range(0,la+1)]for i in range(0,lb+1)]
    #for i in l:
        #print i
    for i in range(1,lb+1):
        for j in range(1,la+1):
            if(a[j-1]==b[i-1]):
                #print a[j-1]," ",b[i-1]
                l[i][j]=l[i-1][j-1]+1
            else:
                #print i," ",j," ",l[i][j]
                if l[i][j-1]>=l[i-1][j]:
                    l[i][j]=l[i][j-1]

                else: #l[i][j-1]>l[i-1][j]:
                    l[i][j]=l[i-1][j]
                #else:
                 #   print "sths wrong"
    
    #for i in l:
        #print i
    return l[lb][la]




#for weight
def weight(x):
    #print"001111111100000000000000000000000000000000000000000000000"
    m=len(x)
    l={}
    ht={}
    #directoryPath = r'C:\Python27\Doc'
    #os.mkdir('ques')
    fl=str(x) + ".txt"
    
    l=csv.reader(open('IDF.txt','r'))
    for k in l:
        y=k[0]
        n=len(y)
        lcs=float(lcsf(x,y))
        if m>=n:
            maxx=m
        else:
            maxx=n
        
        zzz=float(lcs)/float(n)           #threshold
        smr=float((2*lcs)/float((m+n)))
        if zzz>0.3 and zzz!=1:
            idf=float(k[1])
            lcsr=float(lcs)/float(maxx)
            ld=len(y)-lcs
            z=smr*idf
            wght=(float(lcsr)*z)/float(ld)
            ht[y]=wght
            print y,ht[y]
        elif zzz==1: #and smr==1:
            idf=float(k[1])
            wght=idf/.1
            ht[y]=wght
            print y,ht[y]
        else:
            print y,'0',zzz,smr,lcs
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
    #os.remove(fl)
    c=0
    #ulta={}
    new=csv.writer(open('Final/'+fl,'a'))
    ind=0
    
    for kk in vli:
        for i in nht[kk]:
            if (len(i)>=int(len(x)*.70)and lcsf(x,i)>int (.50*len(i))):
                new.writerow([i,kk])
'''
    c=0
    for key,val in ulta:

    
        try:
            p=open('c:/Python27/final/'+fl,'r')
        except:
            if(c<5):
            
                new=csv.writer(open('c:/Python27/final/'+fl,'a'))
                new.writerow([kk,nht[kk]])    
                c+=1
            else:
                break
'''
       # for key,val in ht.items():
        #    new.writerow([key,'   ',val])
    
def posy(word,qposs):
    re=csv.reader(open('Final/'+word+'.txt','r'))
    for  i in re:
        len_v=len(i[0])
        word=i[0]
        for k in qposs.keys():
            s=k.encode('UTF-8')
            l=s.split(' ')
            for w in l:
               if(len(w)==len_v and w[0]==word[0] and w[len_v-1]==word[len_v-1] and w==word):
                    qposs[k]+=float(i[1])
                    break
    return qposs

def qpos10(ques,qposs):
    h={}
    #print ques
    for k in qposs.keys():
        if (len(k)<1.5*len(ques)):

            try:
                h[qposs[k]].append(k)
            except:
                h[qposs[k]]=[]
                h[qposs[k]].append(k)
    l=sorted(h.keys(),reverse=True)
    ind=0
    qtions=[]
    for i in l:
        for q in h[i]:
            qtions.append(q)
            print q,i
            print '\n****************************\n'
            ind+=1
            if(ind>=10):
                return qtions
        
        

#########################################################################
def main():
    qposs={}
    msg=raw_input()
    msg=re.sub(r"[^a-zA-Z0-9\n%]",r" ",msg)
    msg=msg.lower()
    re=pickle.load(open('AllQues.txt','r'))
    for i in re:
        qposs[i]=float(0)
    token=msg.split(' ')
    
    #a=os.mkdir('c:\Python27\SMS_question')
    for i in token:
        try:
            s='c:/Python27/final/'+str(i)+'.txt'
            p=open(s,'r')
            qposs=posy(i,qposs)
            continue
        except:
            weight(i)
            qposs=posy(i,qposs)
    print '\n#########################\n'
    l=qpos10(msg,qposs)
 
    
