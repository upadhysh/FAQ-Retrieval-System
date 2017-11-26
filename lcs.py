
def sub(a,b):
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
                    
    for i in l:
        print i
    return l[lb][la]
