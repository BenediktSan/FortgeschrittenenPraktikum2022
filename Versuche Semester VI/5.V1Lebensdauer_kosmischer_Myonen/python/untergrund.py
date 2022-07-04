import numpy as np 

def poisson(k, l, Ts):
    return (l*Ts)**k/(np.math.factorial(k))*np.exp(-l*Ts)

N_end = np.genfromtxt('python/data/v01-messwerte.Spe', skip_header =5, unpack=True)


t=272190
N=3256768
l=N/t #Ereignisse im Detektor in Suchzeit
print(l)
print(f"\nStartsignale: {N}\n Messzeit: {t} s = {t/3600} h\nEndsignale: {N_end.sum()}")

Ts  =   10**(-6) #Suchzeit 
k   =   1        #Ereignisszahl

p=0
for i in range(100):
    p=p+poisson(i+1,l,Ts)
print(f"Wahrscheinlichkeit, dass mindestens ein Muon während Suchzeit eintritt liegt bei {p*100:.4}%\n")

print(f"Es wurden {N*p} Myonen falsche gemessen")
print(f"pro Kanal also {N*p/512:.3}")