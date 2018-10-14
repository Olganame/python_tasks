#!/usr/bin/env python
# coding: utf-8
#12. Create a script called shortcut to remove all the lowercase vowels in a given string.

#Examples:
#shortcut("codewars") # --> cdwrs
#shortcut("goodbye")  # --> gdby

# In[37]:


def add_length(sstr):
    mas = sstr.split()
    for idx, item in enumerate(mas): 
        mas[idx] = '{0} {1}'.format(item, len(item))
    return mas


# In[38]:


print(add_length('apple ban'))


# In[39]:


print(add_length('you will win'))

