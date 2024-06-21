import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

n = int(input('Количество делений:'))
data = []
for el in range(n):
    data.append(1)
cs=cm.rainbow(np.arange(n)/n)


plt.pie(data, colors=cs)
plt.show()
