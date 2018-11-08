#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shortcut(line):
    return "".join( c for c in line if c not in "a,e,i,o,u" )


# In[2]:


print(shortcut("codewars"))


# In[3]:


print(shortcut("goodbye"))


# In[ ]:




