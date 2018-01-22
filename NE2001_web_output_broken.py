# coding: utf-8

import matplotlib.pyplot as plt

freqs = [0.728, 1.0, 1.4, 3.1]
web = [6.18E3, 9.81E3, 0.03E6, 10.92E6]
real = [2.42E3, 9.81E3, 43.12E3, 1.42E6]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(freqs, web, label="web")
ax.scatter(freqs, real, label="real")
ax.legend()
ax.set_yscale("log")
ax.set_xscale("log")
ax.grid()
ax.set_xlabel("Centre frequency [GHz]")
ax.set_ylabel(r"$\Delta \nu_\mathrm{DISS}$ [Hz]")
ax.set_ylim(2.3E3, 11E6)
ax.legend(loc="upper left")

plt.savefig("NE2001_comparison.png",
dpi=200,
bbox_inches="tight")

plt.show()
