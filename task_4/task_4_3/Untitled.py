#!/usr/bin/env python
# coding: utf-8

# In[26]:


def elementwise(fn):
    def newfn(arg):
        if hasattr(arg,'__getitem__'):  
            return type(arg)(map(fn, arg))
        else:
            return fn(arg)
    return newfn


# In[28]:


@elementwise
def compute(x):
    return x**2 - 1


# In[30]:


print(compute(2))


# In[31]:


print(compute([1,2,3]))

