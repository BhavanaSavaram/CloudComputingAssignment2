#!/usr/bin/env python
# coding: utf-8


import os
from collections import Counter
import socket

#code for printing names of txt files in given directory
result=""
for f in os.listdir("./"):
    if f.endswith(".txt"):
        temp=(os.path.join(".", f))
        temp=temp[2:]
        result+=temp+","
result=result[:-1]


#code for printing total word count
wordCount=0
for i in result.split(","):
    with open( i , 'r') as f:
        p = f.read() 
        words = p.split()
        wordCount += len(words)
result+="\nTotal word count :"+ (wordCount.__str__())+"\n"


# In[77]:

#code for printing top3 reccuring words
result+=f"Top 3 words in IF.txt are:\n"
with open( 'IF.txt' , 'r') as f:
    p = f.read() 
    words = p.split()
    N = 3
    c = Counter(words)
    for w, count in c.most_common(N):
        result+=(w)+" , "+(count.__str__())+"\n"


#code for printing IP address
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
result+="Your Computer IP Address is:" + IPAddr.__str__()



file1 = open('/home/output/result.txt', 'w')
file1.write("txt files present in directory are ")
file1.write(result)
file1 = open('/home/output/result.txt', 'r')
print(file1.read())
file1.close()







