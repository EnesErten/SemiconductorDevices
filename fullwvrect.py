import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1e-2 , 1e-5)
ac_signal = 10 * np.sin(2 * np.pi * 1e3 * t)
output = []

for i in ac_signal:
    if abs(i) >= 0.7:
        output.append(abs(i) - 0.7 )

    else:
        output.append(0)

plt.plot(t,output)
plt.plot(t, ac_signal)
plt.grid()
plt.show()

area = np.trapz(output, t)
print("The area of the output signal(integral of the output signal mutliply with -1)\n>>", str(area))
print("The average of the output signal.\nIntegral of the signal / time range\n>>", str(area / 1e-2))