#!/usr/bin/env python
# coding: utf-8

# In[18]:


def shortcut(line):
    line = "".join( c for c in line if c not in "a,e,i,o,u" )
    return line


# In[19]:


print(shortcut("codewars"))


# In[20]:


print(shortcut("goodbye"))

