import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
import os

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")



def gerade(x, m, b):
    return m * x + b


t, K = np.genfromtxt("python/data/kalibration.dat", unpack=True)

params, covariance_matrix = np.polyfit(K, t, deg=1, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Ausgeben der Parameter
print("\nRegressionsparameter für Kalibration")
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = ({value*10**3:.8f} ± {error*10**3:.8f})ns")

x = np.linspace(np.min(K), np.max(K))
plt.plot(x, gerade(x, *params), "k", linewidth=1, label="lineare Regression")
plt.plot(K, t, "r+", markersize=10, label="Daten")
plt.xlabel(r"Channel")
plt.ylabel(r"$\Delta t$ / $ \mu s$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plots/kalibration.pdf")
