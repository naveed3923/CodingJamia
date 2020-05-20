#!/usr/bin/env python
# coding: utf-8

# In[16]:


# given two arrays A & B of positive integers. Your Task is to find numbers which are present in the first array but not
# present in the second array.

def not_present(A,B):
    res=list()
    result=list()
    for i in A:
        if i not in B:
            res.append(i)
    result=sorted(res)
    return result

print(not_present([1,2,3,4,5,10],[2,3,1,0,5]))
print(not_present([1,4,5,6,7,11,12,9],[1,4,5,13,15,16,25]))


# In[ ]:





# In[ ]:




