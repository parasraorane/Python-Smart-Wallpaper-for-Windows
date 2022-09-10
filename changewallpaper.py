#!/usr/bin/env python
# coding: utf-8

# In[26]:


import ctypes
import numpy as np
import os
z=os.listdir("D:/Pictures/slideshow")
path=z[np.random.randint(len(z))]
ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:/Pictures/slideshow/"+path , 0)

