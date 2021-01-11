#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import matplotlib.pyplot as plt 


# In[31]:


# 4.1
x = np.linspace(-5, 5, 100)
y1 = x**2 - 1
y2 = (np.exp(x) + x - 1)/x
plt.plot(x,y1)
plt.plot(x, y2)


# In[26]:


from scipy.optimize import fsolve

def equations(p):
    x, y = p 
    return (x**2 - 1 - y, np.exp(x) + x - x*y - 1)

x1, y1 = fsolve(equations, (-2, 0))
x2, y2 = fsolve(equations, (2, 3))
x3, y3 = fsolve(equations, (4, 15))
print(x1, y1)
print(x2, y2)
print(x3, y3)


# In[90]:


# 4.2
x = np.linspace(-3, 7, 100)


fig,ax = plt.subplots()
y1 = x**2 - 1
ax.plot(x,y1)

y2 = (np.exp(x) + x - 1)/x
ax.plot(x, y2)

y3 = (np.exp(x) + x - 1000)/x
ax.plot(x, y3)

ax.fill_between(x, y2, y3, color ="yellow")
plt.ylim(-30, 50)


# In[100]:


from scipy.optimize import fsolve
x = np.linspace(-5, 10, 100)

def equations(p):
    x, y = p 
    return (x**2 - 1 - y, np.exp(x) + x - x*y - 1)

x1, y1 = fsolve(equations, (-2, 0))
x2, y2 = fsolve(equations, (0, 0))
x3, y3 = fsolve(equations, (2, 0))
x4, y4 = fsolve(equations, (4, 10))

print(f"Все точки расположенные в желтой области и принадлежащие графику y = x**2 - 1 (кроме самих точек пересечения),\n"
f" где x < {x1} и y > {y1}, \n"
f"где {x2}< x < {x3} и {y2}< y < {y3} \n"
f"и  x > {x4} и y > {y4} ")


# In[ ]:




