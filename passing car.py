#!/usr/bin/env python
# coding: utf-8

# In[1]:


A=[0,1,0,1,1,0,1,0]
q=len(A)
l=list()
z=list()
for i in range(0,q):
    if A[i]==0: 
        l.append(i)
    elif A[i]==1:
        z.append(i)
o=[[a,b]for a in l for b in z if a!=b and a<b]
k=len(o)
if k>0:
    print(k)
else:
    print(-1)
print(o)


# In[ ]:




