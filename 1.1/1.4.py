#!/usr/bin/env python
# coding: utf-8

# In[44]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[45]:


x = np.linspace(0, 10, 50)
plt.plot(x, np.cos(1 * x))

y = np.linspace(0, 10, 50)
plt.plot(y, np.cos(1.3 * x))
print(x, y)


# In[ ]:




