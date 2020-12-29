#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[25]:


fig, ax = plt.subplots()
ax = Axes3D(fig)
X = np.arange(-7, 7, 2)
Y = np.arange(-7, 7, 2)
ax.view_init(15, -0)

X, Y = np.meshgrid(X, Y)

Z = 0.5*X + 2*Y + 33
Z2 = 0.5*X + 2*Y 
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z2)
plt.show()


# In[89]:


fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(15, 45)
X = np.arange(-50, 50, 2)
Y = np.arange(-50, 50, 2)
X, Y = np.meshgrid(X, Y)

Z = ((X**2)/0.4 + (Y**2)/3)
Z2 = ((X**2)/1 - (Y**2)/1)
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z2)
ax.scatter(0, 0, 0,'z',50,'red')
plt.show()


# In[ ]:




