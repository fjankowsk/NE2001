# coding: utf-8

import matplotlib.pyplot as plt

freqs = [0.728, 1.0, 1.4, 3.1]
web = [6.18e3, 9.81e3, 0.03e6, 10.92e6]
real = [2.42e3, 9.81e3, 43.12e3, 1.42e6]

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
ax.set_ylim(2.3e3, 11e6)
ax.legend(loc="upper left")

plt.savefig("NE2001_comparison.png", dpi=200, bbox_inches="tight")

plt.show()
