from xml.dom import minidom
import re
x=minidom.parse("eng.xml")
faqs=x.getElementsByTagName("FAQS")[0]
faq=faqs.getElementsByTagName("FAQ")

l=[]
for Q in faq:
    q=Q.getElementsByTagName("QUESTION")[0].firstChild.data  #extracting questions
    q=q.lower() #converting to lower case
    q=re.sub(r"[^a-zA-Z0-9\n]",r" ",q)    #removing special charecters
    if(isinstance(q,unicode)):  #removing unicode
        q=q.encode('UTF-8')
    l.append(q) #making a list

"Making a dump File"

import pickle
pickle.dump(l,open("AllQues.txt","w"))
