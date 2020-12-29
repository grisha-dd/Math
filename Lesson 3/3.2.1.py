#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import matplotlib.pyplot as plt 


# In[18]:


x = np.linspace(-3*np.pi, 3*np.pi, 200)

y = 1 * np.cos(x - 2) + 3
y2 = 2  * np.cos(x - 3.5) + 0.9
y3 = 0.2 * np.cos(x - 5.9)+ 0

fig, ax = plt.subplots()
ax.plot(x, y, color = "blue", linewidth = 2)
ax.plot(x, y2, color = "r", linewidth = 2)
ax.plot(x, y3, color = "g", linewidth = 2)


# In[ ]:





# In[ ]:




