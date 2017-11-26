
f=open('Slang.txt','r')
wr=open('Nslang.txt','w')
ctd=0
for i in f:
    s=i
    for x in s:
        if x=='-':
            ctd+=1
    if ctd>1:
        ctd=0
        c=''
        for x in s:
            if x=='-' and ctd==0:
                ctd+=1
                continue
            else :
                c+=x
        s=c
    ctd=0
    wr.write(s)
