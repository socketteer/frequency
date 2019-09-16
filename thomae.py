import manifest
import matplotlib.pyplot as plt


N = 100
x = []
y = []

for i in range(1, N):
    for j in range(1, i):
        x.append(j / i)
        y.append(manifest.gcd_method(i, j))

plt.plot(x, y, marker=',', linestyle='')


plt.xlabel('true frequency')
plt.ylabel('manifest frequency')
plt.show()
