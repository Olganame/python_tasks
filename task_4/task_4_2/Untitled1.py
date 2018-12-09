#!/usr/bin/env python
# coding: utf-8

# In[34]:


def decorator(tag):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            return "<"+tag+">"+func(*args, **kwargs)+"</"+tag+">"
        return wrapper
    return real_decorator


# In[35]:


@decorator("h1")
@decorator("b")
@decorator("i")
def func(text):
    text += "!"
    return text


# In[36]:


func("hello")

