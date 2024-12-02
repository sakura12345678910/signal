import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-3, 3, 1000)
plt.plot(t, np.exp(-t**2)*np.sin(20*t))
plt.show()