# GRAPHICAL ANALYSIS USING THE EXPONENTIAL MODEL
import numpy as np
import matplotlib.pyplot as plt
import math

N = 1.65
T = 26.85
q = 1.6e-19
k = 1.38e-23
Iss = 220e-12
e = math.exp(1)
Vs = 10
R = 500

Vt = k * (T + 273) / q  # thermal voltage

Vd = np.linspace(0, 0.8, 1001)  # voltage range 0 to 0.8 volts

Id = Iss * (e ** (Vd / (N * Vt)) - 1)
# characteristics graph of the diode

load_line = (Vs - Vd) / R
# load line graph

plt.plot(Vd, Id)
plt.plot(Vd, load_line)

a = Id - load_line

b = 0

for i in range(0, 1001):
    if a[i] < 1e-20:
        b = i

print("Q point is", Id[b], Vd[b])

plt.show()
