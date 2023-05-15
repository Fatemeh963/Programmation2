#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.DataFrame([{'product_id':23, 'name':'computer', 'wholesale_price': 500,
        'retail_price':1000, 'sales':100},
        {'product_id':96, 'name':'Python Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':1000},
        {'product_id':97, 'name':'Pandas Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':500},
        {'product_id':15, 'name':'banana', 'wholesale_price': 0.5,
        'retail_price':1, 'sales':200},
        {'product_id':87, 'name':'sandwich', 'wholesale_price': 3,
        'retail_price':5, 'sales':300},
        ])
df


# In[7]:


#calculer le revenue totale

((df['retail_price'] - df['wholesale_price']) * df['sales']).sum()







# In[9]:


df['current_net'] = [50000.0, 40000.0, 20000.0, 100.0, 600.00]


df


df['after_15'] = df['current_net'] * 0.85
df




# In[10]:


df['after_25'] = df['current_net'] * 0.75
df


# In[11]:


df['after_20'] = df['current_net'] * 0.8
df


# In[13]:


df [['after_15','after_25', 'after_25']].sum()


# In[15]:


df['current_net'].sum()- df[['current_net','after_15','after_25', 'after_20']].sum()


# In[ ]:




