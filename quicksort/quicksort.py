#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
        q = random.choice(nums)
        l_nums = [n for n in nums if n < q] 
        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return quicksort(l_nums) + e_nums + quicksort(b_nums)


# In[15]:


print(quicksort([1, 10 , 3, -1]))


# In[ ]:




