from turtle import color
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-6, 6, 0.01)

def boltzman(x, xmid, tau):
    return 1. / (1. + np.exp(-(x-xmid) / tau))

S = boltzman(x, 0, 1)
Z = 1 - boltzman(x, 0.5, 1)

plt.plot(x, S, x, Z, color='red', lw=2)
plt.fill_between(x, Z, color='blue', alpha=0.5)
plt.show()