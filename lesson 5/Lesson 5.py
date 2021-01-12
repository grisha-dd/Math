#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt 


# In[12]:


# 5.1 Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).
x = int(input("Сколько раз запускаем рулетку? "))
count = 0
while count < x:
    field = np.random.randint(0, 37)
    print(f"Выпало поле: {field}")
    count += 1


# In[49]:


# 5.2.1 Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или подбрасывания монетки.

# вероятность совместного появления независимых событий равна произведению вероятностей этих событий

def eq_p(m, n):
    return m / n


def p_multi(p1, p2):
    return p1 * p2


# p = m/n
FIELD_1 = 6
FIELD_2 = 29
n = 37

m1 = 1
print(f"Поле {FIELD_1} может выпать {m1} раз")

m2 = 1
print(f"Поле {FIELD_2} может выпать {m2} раз")

p1, p2 = eq_p(m1, n), eq_p(m2, n)
print(f"Вероятность выпадения поля  {FIELD_1}: {p1} ")
print(f"Вероятность выпадения поля  {FIELD_2}: {p2} ")

multi_prob = p_multi(p1,p2)
print(f"Вероятность выпадения поля {FIELD_2} после поля {FIELD_1} : {multi_prob} ")

print(f"\nПроверяем, крутим рулетку:")
times = 100000
a = list(np.random.randint(0, 37, times))
b = list(np.random.randint(0, 37, times))
k = 0
for index, field in enumerate(a):
    if field == 6 and b[index] == 29:
        k += 1
print(f"В {k} случае(-ях) из {times} раз выпало поле {FIELD_1} и затем поле {FIELD_2}")
print(f"Вероятность составила {eq_p(k,times)}, что приближено к результату произведения {multi_prob}")


# In[46]:


# 5.2.2 Сгенерируйте десять выборок случайных чисел х0, …, х9. и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.
final = []
num_bins = 20
for i in range(0,1000):
    final.append(sum(np.random.randint(0,100,10)))
n, bins, patches = plt.hist(final, num_bins)

plt.title('Histogram')


# In[53]:


# 5.3.1
# Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей 
# (через биномиальное распределение) и сравните результаты.

from math import factorial

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
p_monte = k / n
print(f"Метод-Карло: k = {k}, n = {n}, k/n = {p_monte}")

n = 4
k = 2

C = (factorial(n) / (factorial(k) * factorial(n - k)))
p_bernuli = C * (1 / 2 ** n)
print(f"Формула Бернулли: {p_bernuli} при k = {k}, n = {n},")
print(f"Разница результатов: {abs((p_bernuli-p_monte)/p_bernuli)*100:.2}%")


# In[69]:


# 5.3.2
# Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности из n независимых испытаний, 
# взяв другие значения n и k.

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 4:
        k = k + 1
p_monte = k / n
print(f"Метод-Карло: k = {k}, n = {n}, k/n = {p_monte}")

n = 5
k = 4

C = (factorial(n) / (factorial(k) * factorial(n - k)))
p_bernuli = C * (1 / 2 ** n)
print(f"Формула Бернулли: {p_bernuli} при k = {k}, n = {n},")
print(f"Разница результатов: {abs((p_bernuli-p_monte)/p_bernuli)*100:.2}%")


# In[85]:


k, n = 0, 1000000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 5:
        k = k + 1
p_monte = k / n
print(f"Метод-Карло: k = {k}, n = {n}, k/n = {p_monte}")

n = 5
k = 5

C = (factorial(n) / (factorial(k) * factorial(n - k)))
p_bernuli = C * (1 / 2 ** n)
print(f"Формула Бернулли: {p_bernuli} при k = {k}, n = {n},")
print(f"Разница результатов: {abs((p_bernuli-p_monte)/p_bernuli)*100:.2}%")


# In[120]:


# 5.4. 
# Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты перестановок для других значений n и k
import itertools
# перестановка
count = 0
k = 5
n = "abcde"
for p in itertools.permutations(n,k):
    print(''.join(str(x) for x in p))
    count += 1
print(f"Total : {count}")
A = factorial(len(n))
print(f"Check: A = n! = {len(n)}! = {A}")


# In[121]:


# размещение
count = 0
k = 3
n = "abcde"
for p in itertools.permutations(n,k):
    print(''.join(str(x) for x in p))
    count += 1
print(f"Total : {count}")
A = int(factorial(len(n))/factorial(len(n)-k))
print(f"Check: A = n!/(n-m)! = {len(n)}!/({len(n)}-{k})! = {A}")


# In[130]:


# сочетание
count = 0
k = 3
n = "abcde"
for p in itertools.combinations(n,k):
    print(''.join(str(x) for x in p))
    count += 1
print(f"Total : {count}")
A = int(factorial(len(n)) / (factorial(k) * (factorial(len(n)-k))))
print(f"Check: A = n!/(k!*(n-k))! = {len(n)}!/({k}!*({len(n)}-{k})!) = {A}")


# In[144]:


# 5.5
# Дополните код расчетом коэффициента корреляции x и y по формуле

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])
plt.show()


# In[146]:


avrX =np.mean(x)
avrY = np.mean(y)
R = (sum((x-avrX)*(y-avrY)))/((sum((x-avrX)**2) * sum((y-avrY)**2)) ** (1/2))
print(f"Коэффициент корреляции по формуле: {R}")
R_check= np.corrcoef(x, y)
print(f"Check: {R_check}")


# In[ ]:




