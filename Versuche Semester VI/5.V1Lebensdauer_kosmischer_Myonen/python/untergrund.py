import numpy as np 
import uncertainties as unc
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


def poisson(k, l, Ts):
    return (l*Ts)**k/(np.math.factorial(k))*np.exp(-l*Ts)

N_end = np.genfromtxt('python/data/v01-messwerte.Spe', skip_header =5, unpack=True)


t=272190            #gesamtzeit
N=3256768
uN = unc.ufloat(N,np.sqrt(N))
l=uN/t #Ereignisse im Detektor in Suchzeit
print("dursch Zählrate: ",l)

print(f"\nStartsignale: {noms(uN)} \pm {stds(uN)}\nMesszeit: {t} s = {t/3600} h\nEndsignale: {N_end.sum()}")

Ts  =   10**(-5) #Suchzeit 
print(f"lambda = ({l *Ts*10**3}) e-3")

l=noms(l)

p=0
for i in range(100):
    p=p+poisson(i+1,l,Ts)
print(f"Wahrscheinlichkeit, dass mindestens ein Muon während Suchzeit eintritt liegt bei {p*100:.4}%\n")
print(f"P_ges = {p}")
print(f"P(1) = {poisson(1,l,Ts)}")
print(f"Es wurden {N*p} Myonen falsche gemessen")
print(f"pro Kanal also {N*p/512:.3}")