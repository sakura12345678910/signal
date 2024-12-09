import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

# 矩形波の立ち上がるところだけの信号
def clk(t):
    if t >= 0:
        return 1
    else:
        return -1

# np.linspaceで用意したndarrayを引数にできるようにベクトル化
npclk = np.vectorize(clk)

# フーリエ級数の部分和（途中で打ち切ったもの）
# これはnp.sin()関数に使われるためndarrayを引数にでき，ベクトル化しなくてよい
def partialsum(t, n):
    sum = 0
    for i in range(1, n+1):
        sum += (4 / PI) * np.sin((2 * i-1)*t) / (2 * i - 1)
    return sum

t = np.linspace(-PI, PI, 1000)

plt.plot(t, npclk(t))
plt.plot(t, partialsum(t, 5))
plt.show()