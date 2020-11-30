import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2, 1e-5)
# time range 0 to 1e-2 with 1e-5 step
ac_signal = 4 * np.sin(2 * np.pi * 1e3 * t)  # sinusoidal ac signal


# creating half wave signal
def h_wave(signal):
    half_wave_rsig = []

    for i in signal:
        if i <= 0 or i <= 0.7:
            half_wave_rsig.append(0)
            # if signal is negative
            # or less than 0.7 volts

        else:
            half_wave_rsig.append(i - 0.7)
            # if signal is positive and greater than 0.7 volts

    return half_wave_rsig
    # return half wave signal


output = h_wave(ac_signal)
# output voltage

plt.plot(t, ac_signal, '-b', label="AC Input Voltage")
plt.plot(t, output, '-r', label="Output Voltage")
leg = plt.legend()
plt.show()
# plot the signals

area = np.trapz(output, t)
print("The area of the output signal(integral of the output signal)\n>>", str(area))
print("The average of the output signal.\nIntegral of the signal / time range\n>>", str(area / 1e-2))
# calculate the integral and average signal
