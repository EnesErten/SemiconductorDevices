import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1e-2, 1e-5)
ac_signal = 4 * np.sin(2 * np.pi * 1e3 * t)


def h_wave(signal):
    half_wave_rsig = []

    for i in signal:
        if i > 0.7:
            half_wave_rsig.append(0.7)

        elif 0.7 >= i > 0:
            half_wave_rsig.append(i)

        else:
                half_wave_rsig.append(i)
    return half_wave_rsig


output = h_wave(ac_signal)

plt.plot(t, ac_signal, '-b', label="Input Voltage")
plt.plot(t, output, '-r', label="Output Voltage")
leg = plt.legend()
plt.show()

area = abs(np.trapz(output, t))
print("The area of the output signal(integral of the output signal mutliply with -1)\n>>", str(area))
print("The average of the output signal.\nIntegral of the signal / time range\n>>", str(area / 1e-2))