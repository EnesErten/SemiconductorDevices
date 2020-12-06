import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1e-2, 1e-5)
ac_signal = 10 * np.sin(2 * np.pi * 1e3 * t)
output = []

for i in ac_signal:
    if abs(i) >= 0.7:
        output.append((4 * abs(i)) / 7)

    else:
        output.append(0)

plt.plot(t, output,'r',label = 'Output Voltage')
plt.plot(t, ac_signal,'b',label = 'Input Voltage')
plt.grid()
plt.legend()
plt.show()
