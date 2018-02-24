import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0, 1], [1, 3], [2, 2], [3, 5], [4, 7], [5, 8], [6, 8], [7, 9], [8, 10], [9, 12]])
x = np.array([0, 1, 2, 3, 4, 5, 6, 7 , 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
x_mean = np.mean(x)
print(x_mean)
y_mean = np.mean(y)
print(y_mean)
xx = x - x_mean
yy = y - y_mean

print(xx)
print(yy)

xy = xx * yy
print(xy)

xx_sqr = xx * xx
print(xx_sqr)

ssxy = np.sum(xy)
ssxx = np.sum(xx_sqr)
print(ssxy)
print(ssxx)

b1 = ssxy/ssxx
print(b1)

b0 = y_mean - b1*x_mean
print(b0)

# i = np.linspace(np.min(x)-1, np.max(x)+1, 1000)
j = b0 + b1 * x

plt.scatter(x, y, color='blue')
plt.plot(x, j, color='red')
plt.show()

