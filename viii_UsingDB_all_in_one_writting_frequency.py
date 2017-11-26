
import sqlite3
import re
import csv
import csv
import os
#Combine
def query(a):
    a=re.sub(r"[^a-zA-Z0-9\n]"," ",a)
    l=a.split()
    for i in l:
        try:
            os.remove('top.txt')
        except:
            l=0
        match(i)
        

def match(a):
    re=csv.reader(open("IDF.txt","r"))
    a=a.lower()
    #os.mkdir(a)
    conn=sqlite3.connect('DB.db')
    try:
        conn.execute('''DROP TABLE WORDS ;''')
    except:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    conn.execute('''CREATE TABLE WORDS(WORD CHAR(50) NOT NULL,LCSR TEXT NOT NULL,SR TEXT NOT NULL,LEV TEXT NOT NULL,WW TEXT NOT NULL);''')
    for l in re:
        x=sub(l[0],a,conn,l[1])
        if x==1:
            break
        #conn.
    conn.commit()
    if x!=1:
        top(a)
    show(a)


def sub(a,b,conn,idf):
    sub_s=0
    p=0
    i=j=0
    la=len(a)
    lb=len(b)
    while j<lb:
        if i==la:
            i=p
            j+=1
        elif a[i]==b[j]:
            sub_s+=1
            p=i
            j+=1
        i+=1
    if(la>lb):
        m=la
    else:
        m=lb
        m=float(m)
    ld=m-sub_s    
    if(float(sub_s)>=float(2*int(lb)/3) and ld<3):
        lcsr=float(sub_s/m)
        sr=float(2*sub_s)/float(la+lb)
        
        if( ld == 0 ):
            s=str(b)+'.txt'
            f=open('top.txt','w')
            f.writelines(str(a)+","+str("zzzzz\n"))
            return 1
        ww=lcsr*sr*float(idf)
        #print ww
        ww=ww/ld
        if isinstance(a,unicode):
            a.encode('UTF-8')
        conn.execute("INSERT INTO WORDS (WORD,LCSR,SR,LEV,WW) VALUES('"+str(a)+"',"+str(lcsr)+","+str(sr)+","+str(ld)+","+str(ww)+");")
        conn.commit()
    return 0


def top(i):
    h={}
    conn=sqlite3.connect('DB.db')
    r=conn.execute('SELECT * FROM WORDS')
    for e in r:
        h[e[4]]=[]
    r=conn.execute('SELECT * FROM WORDS')
    for e in r:
        h[e[4]].append(e[0])
    l=sorted(h.keys(),reverse=True)
    w=csv.writer(open('top.txt','a'))
    for i in l:
        #print i
        w.writerow([h[i],i])


def show(a):
    j=0
    r=csv.reader(open('top.txt','r'))
    name=str(a)+'.txt'
    try:
        os.remove(name)
    except:
        o=''
    finally:
        f=open(name,'w')
    for i in r:
        o=i[0]
        o.strip("[]")
        o=o.replace("u'","")
        o=o.replace("'","")
        o=o.replace("[","")
        o=o.replace("]","")
        l=o.split(',')
        #print l
        for i in l:
            i=i.replace(" ","")
            print i
            f.writelines(i+'\n')
            j=j+1
            if j>=5:
                return
