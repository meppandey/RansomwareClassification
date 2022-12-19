#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
path = r"C:\Users\pr14p\Desktop\Small Data\new\aa"

file_list = glob.glob(path + "/*.csv")
print('File names:', file_list)

pd.concat(map(pd.read_csv, file_list), 
          ignore_index=True).to_csv('aa.csv',index=False)


# In[ ]:




