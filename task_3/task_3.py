#!/usr/bin/env python
# coding: utf-8

# In[31]:


def find_repetitions(input_str):
    result_str  = ''
    for line in open(input_str):
        result_str += line.strip()
        result_str += ' '
    print(result_str)
    mas = result_str.split(' ')
    del(mas[len(mas)-1])
    mas_repetitions = {}
    mas_index = []
    while len(mas) > len(mas_index):
        if len(mas_index) > 0:
            s = mas[min([i for i,j in enumerate(mas) if i not in mas_index])]
        else: 
            s = mas[0]
        i = 0 
        for idx,item in enumerate(mas): 
            if idx not in mas_index:
                if s.lower() == item.lower():
                    i += 1
                    mas_repetitions[s] = i
                    mas_index.append(idx)
    count = max(mas_repetitions.keys(), key=(lambda k: mas_repetitions[k]))
    return ('{0} {1}'.format(count, mas_repetitions[count]))


# In[32]:


print(find_repetitions('file.txt'))


# In[ ]:





# In[ ]:





# In[ ]:




