import csv
def so():
    r=csv.reader(open("Match.txt","r"))
    h={}
    l=[]
    for i in r:
        h[i[0]]=i[1]
        l.append(i[0])
        print l
    l=sorted(l)
    print l
