# Author:SONG
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import random

x = np.linspace(0, 100, 1000)  # (最低值，最高值，细粒度)
y = x + 10 * np.sin(5 * x) + 7 * np.cos(4 * x)
plt.plot(x, y)


