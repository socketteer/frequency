import manifest
import matplotlib.pyplot as plt
import numpy as np

x = []
y1 = []
y2 = []

for frequency in np.arange(0.0, 3, 0.005):
    x.append(frequency)
    y1.append(manifest.gcd_method(1, frequency))
    y2.append(manifest.remainder_method(1, frequency))

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlabel('true frequency')
plt.ylabel('manifest frequency')
plt.title('aliasing')
plt.show()
