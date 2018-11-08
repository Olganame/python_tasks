#!/usr/bin/env python
# coding: utf-8

# In[9]:


def add_length(sstr):
    mas = sstr.split()
    return['{0} {1}'.format(item, len(item)) for idx,item in enumerate(mas)]


# In[10]:


print(add_length('apple ban'))


# In[11]:


print(add_length('you will win'))


# In[ ]:




