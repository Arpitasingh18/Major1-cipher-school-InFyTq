#!/usr/bin/env python
# coding: utf-8

# In[1]:


def two_sum(nums,target):
    d = {}
    for n,x in enumerate(nums):
        try:
            return [d[x], n]
        except KeyError:
            d.setdefault(target - x,n)

nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))


# In[ ]:




