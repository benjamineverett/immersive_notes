import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html

# sns.set(color_codes=True)
# np.random.seed(sum(map(ord,'distributions')))
# x = np.random.normal(size=100)
# sns.kdeplot(x,shade=2)
# sns.plt.show()

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

fig = plt.figure(figsize=(8,6), dpi=80)

plt.subplot(1,1,1)

C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color='blue', linewidth=1.0, linestyle='-', label = 'Cosine')
plt.plot(X, S, color='green', linewidth=3.0, linestyle='-', label='Sin')
plt.xlim(-np.pi,np.pi)
plt.ylim(-1,1)
plt.xticks(np.linspace(-np.pi,np.pi,9, endpoint=True))
plt.legend(loc = 'upper left')

t = 2 * np.pi / 3
plt.plot([t,t], [0,np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter(t, np.cos(t), 100, color='blue')

plt.show()
