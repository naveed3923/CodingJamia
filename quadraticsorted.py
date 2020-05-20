#!/usr/bin/env python
# coding: utf-8

# In[1]:


# QUADRATIC FUNCTION

def quadratic_fn(nums,a,b,c):
    solution=list()
    for x in nums:
        soln=a*(x**2)+b*x+c
        solution.append(soln)

    
    a=sorted(solution)
    return a

print(quadratic_fn([-4,-2,2,4],1,3,5))
print(quadratic_fn([-4,-2,2,4],-1,3,5))
print(quadratic_fn([-1,0,2,4],2,4,1))


# In[ ]:




