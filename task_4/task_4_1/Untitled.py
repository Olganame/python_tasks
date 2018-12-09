#!/usr/bin/env python
# coding: utf-8

# In[2]:


def counter(func):
    def wrapper():
        wrapper.count += 1
        res = func()
        print(wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


# In[3]:


@counter
def func():
    print("Hello!")


# In[7]:


func()

