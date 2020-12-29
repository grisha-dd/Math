#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 3.1.2 Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)
import numpy as np

X = int(input("Введите координату начала вектора: "))
Y = int(input("Введите координату конца вектора: "))
L = np.sqrt(X ** 2 + Y ** 2)
print(f"Длина заданного верктора: {L}")


# In[5]:


#  3. Задание (в программе)
# Напишите код на Python, реализующий построение графиков:
# окружности,
# эллипса,
# гиперболы.

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
r = int(input("Введите радиус: "))

x1 = r*np.cos(t)
x2 = r*np.sin(t)

fig, ax = plt.subplots(1)
ax.plot(x1, x2)
ax.set_aspect(1)
plt.show()


# In[4]:


# эллипса,
# х = u+a*cos(t) ; r = v+b*sin(t)
u=0   
v=0    
a=6    
b=3
t = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(1)
plt.plot( u+a*np.cos(t), v+b*np.sin(t) )
ax.set_aspect(1)
plt.show()


# In[ ]:





# In[2]:


# гиперболы.
x = []
y = []
x2 = []
y2 = []

a = 3
b = 6
for i in np.arange(a, 10, 0.01):
    x_ = i
    x.append(x_)
    x2.append(-x_)
    y.append(np.sqrt(((b ** 2) * (x_ ** 2)) / (a ** 2) - (b ** 2)))
    y2.append(-np.sqrt(((b ** 2) * (x_ ** 2)) / (a ** 2) - (b ** 2)))

fig, ax = plt.subplots(1)
plt.plot(x, y, color = "g")
plt.plot(x, y2, color = "g")
plt.plot(x2, y, color = "g")
plt.plot(x2, y2, color = "g")
plt.grid()
plt.ylim(-10, 10)
ax.set_aspect(1)
plt.show()


# In[ ]:




