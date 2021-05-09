 # x and y plot and color bar.
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(100)
y = np.random.rand(100)
size = np.random.rand(100)
color = np.random.rand(100)
plt.scatter(x,y, size, color)
plt.colorbar()
plt.show()
