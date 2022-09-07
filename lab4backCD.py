#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
n=6
x=np.array([0,1,2,3,4,5])
h=x[1]-x[0]
y=np.array([1,11,22,43,75,110])
z=np.zeros((n,n))
for i in range(n):
    z[i][0]=y[i]

b=[]
    
def cdtable():
    for i in range(1,n):
        for j in range(n-i):
            z[j][i]=((z[j+1][i - 1] - z[j][i - 1]))
    return z
z=cdtable()

def xterm(i,value,b):
    pro=1
    for j in range(i):
        pro=pro*(value-b[j])
    return pro

def fact(fac):
    factorial=1
    for i in range(1,fac+1):
        factorial=factorial*i
    return factorial

def formula():
    global a
    a=[]
    for i in range(n):
        d=(n-i)//2
        if(d>0):
            d=d-1
            a.append(z[d][i])
        else:
            a.append(z[d][i])
    print("The values of a0 to a{}:".format(n-1),a)
    mid=int((len(a)/2)-1)
    ahead=mid+1
    back=mid-1
    b.append(x[mid])
    while( len(b)<len(x)):
        b.append(x[back])
        b.append(x[ahead])
        back=back-1
        ahead=ahead+1
    b.pop()
    b.pop()
    print('The values of x0,x(-1),x1,x(-2),x2:',b)
    res=0
    for j in range(1,n):
        res=res+(a[j]/(fact(j)*pow(h,j)))*xterm(j,value,b)
    fres=a[0]+res
    return fres

print("The Table is:\n",z)

value=2.5
fvalue=formula()  
print("The result is:",fvalue)


# In[ ]:




