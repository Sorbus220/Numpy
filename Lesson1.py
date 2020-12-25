#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([[1,6],
            [2,8],
            [3,11],
            [3,10],
            [1,7]])
a


# In[3]:


mean_a = a.mean(axis = 0)
mean_a


# In[4]:


a_centered = a - mean_a
a_centered


# In[5]:


a1 = a_centered[:,0]
a2 = a_centered[:,1]
a_centered_sp = np.dot(a1, a2)
a_centered_sp


# In[6]:


n = a.shape[0]
n


# In[7]:


result = a_centered_sp / (n-1)
result


# In[8]:


np.cov(a.transpose())


# In[9]:


import pandas as pd


# In[11]:


authors = pd.DataFrame({'author_id' : [1, 2, 3], 'author_name' : ['Тургенев', 'Чехов', 'Островский']},
                      columns = ['author_id', 'author_name'])
authors


# In[13]:


book = pd.DataFrame({'author_id' : [1, 1, 1, 2, 2, 3, 3], 'book_title' : ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                      'price' : [450, 300, 350, 500, 450, 370, 290]},
                   columns = ['author_id', 'book_title', 'price'])
book


# In[15]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'inner')
authors_price


# In[16]:


top5 = authors_price.nlargest(5, 'price')
top5


# In[24]:


maxprice = authors_price.groupby('author_name').agg({'price':'max'}).rename(columns={'price' : 'max_price'})
minprice = authors_price.groupby('author_name').agg({'price':'min'}).rename(columns={'price' : 'min_price'})
meanprice = authors_price.groupby('author_name').agg({'price':'mean'}).rename(columns={'price' : 'mean_price'})
authors_stat = pd.concat([maxprice, minprice, meanprice], axis = 1)
authors_stat


# In[ ]:




