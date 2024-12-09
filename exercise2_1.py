import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

PI = np.pi
t = np.linspace(-2*PI, 2 * PI, 1000)

def rect(t, min, max):
    if min <= t and t <= max:
        return 1
    else:
        return 0

nprect = np.vectorize(rect)

z = np.exp(1j * t * nprect(t, -PI, PI))
fig = plt.figure()

x1 = z.real
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(t, x1)

x2 = z.imag
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(t, x2)

plt.show()
```