#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import matplotlib.pyplot as plt 


# In[81]:


# (1,2), (3,10), (5,1)
a = -2.125
b = 12.5
c = -8.375
x = np.linspace(-3, 9, 1000)
y = a * x ** 2 + b * x + c 
fig, ax = plt.subplots()
# ax.set_facecolor("grey")
ax.plot(x, y, color = "blue", linewidth = 2)
POINTS = {1:2, 3:10, 5:1}
ax.scatter(POINTS.keys(), POINTS.values(), color = "orange", linewidth = 3 )
plt.title ("Парабола, проходящая через три точки: (1,2), (3,10), (5,1)")
plt.grid()  
plt.text(-2.5, -65, "y = -2.125 x^2 + 12.5 x - 8.375", fontweight="bold")
for key in POINTS: 
    plt.annotate(f"({key},{POINTS.get(key)})", xy=(key, POINTS.get(key)), xytext=(key-0.5, POINTS.get(key)-10), fontsize=12)


# In[ ]:




