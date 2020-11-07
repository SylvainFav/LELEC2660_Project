'''
Favresse Sylvain, Ledent François, November 2020
LELEC2660 Power Electronics - Project Report
------------------------------------------------
This file contains the main program.
'''

from constants import *
import numpy as np
from matplotlib import pyplot as plt


def find_theta_max():
    theta = np.linspace(1e-3, 1-1e-3, 500)

    f = lambda theta: (1 + theta * (alpha - 1)) / (1 - theta) * Vin
    lim = VDSS_max - margin
    theta_max = (VDSS_max - margin - Vin)/(VDSS_max - margin + (alpha - 1) * Vin)

    plt.plot(theta, [f(t) for t in theta], label=r"$v_{T,\mathrm{max}}$")
    plt.plot(theta, [lim] * len(theta), label=r"$V_{DSS,\mathrm{max}}-m$")
    plt.vlines([theta_max], 0, lim, color="red", linestyles="dashed")
    plt.xlabel(r"$\theta$")
    plt.title(r"$\theta_\mathrm{max} = 0.34605$")
    plt.legend(loc="best")
    plt.xlim(theta[0], theta[-1])
    plt.ylim(0, 2000)
    plt.savefig("fig/find_theta_max.png", dpi=500)
    plt.show()

find_theta_max()
