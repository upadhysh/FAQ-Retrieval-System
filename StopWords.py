import csv


re=csv.reader(open('FreqOfWords.txt','r'))
stop={}
for r in re:
    if(int(r[1])>100 and len(r[0])<=4):
        stop[str(r[0])]=True
w=csv.writer(open('Stop.txt','w'))
for k,v in stop.items():
    w.writerow([k,v])
