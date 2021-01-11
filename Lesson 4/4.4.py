#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import matplotlib.pyplot as plt 


# In[56]:


# sin(а*x)=0
# при условии: 0.01<a<0.02, 100<х<500.
fig,ax = plt.subplots()

from scipy.optimize import fsolve
a = np.linspace(0.01, 0.02, 201)
x = np.linspace(100, 500, 201)

def f(x):
    return (np.sin(0.01*x))
def f2(x):
    return (np.sin(0.02*x))



ax.plot(x, f(x))
ax.plot(x, f2(x))
ax.fill_between(x, f(x), f2(x))


# In[72]:


x = fsolve(f2, 150)

print (x)
x2 = fsolve(f2, 300)
print (x2)
f"Проверяем пересекаются ли в этой точке"
x4 = fsolve(f, 300)
print (x4)


x3 = fsolve(f2, 500)
print (x3)


# In[ ]:




