import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import integrate
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os
from tabulate import tabulate
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")




########MESSWERTE#######

# sorry für den code. i know. its wild

T_0 = -273.15

# T in Kelvin
T_1 = np.array([-44, -42.6, -41.6, -40.1, -38.7, -37.4, -36.0, -34.6, -33.2, -32.0, -30.7, -29.4, -28.1, -26.8, -25.6, -24.4, -23.2, -21.9, -20.7, -19.6, -18.4, -17.2, 
                -15.9, -14.6, -13.4, -12.1, -10.6, -9.2, -7.8, -6.4, -4.9, -3.4, -1.9, -0.5, 0.8, 2.3, 3.7, 5, 6.3, 7.6, 9, 10.3, 11.5, 12.9, 14.2, 15.6, 17, 18.4, 19.8,
                21.3, 22.7, 24.2, 25.7, 27.1, 28.5, 29.9, 31.2, 32.7, 34, 35.4, 36.9, 38.3, 40.5, 41.3, 42.6, 44.1, 45.6, 47.1, 48.6, 50.1  ])
T_1 = T_1 - T_0 #jetzt kelvin

T_2 = np.array([-67.8, -66.8, -65.2, -63.2, -61.2, -59.1, -57.0, -54.8, -52.6, -50.9, -49, -47.2, -45.1, -43, -40.5, -38.3, -36.1, -33.9, -31.9, -30, -28.2, -26.5, 
                -24.8, -23, -21, -19, -17, -15.2, -13.3, -11.5, -9.7, -7.6, -5.5, -3.4, -1.4, 0.6, 2.5, 4.4, 6.5, 8.1, 10.1, 12, 14, 16, 17.9, 19.9, 21.7,
                23.6, 25.4, 27.3, 29.5, 31.7, 33.7, 35.9, 37.7, 39.6, 41.6, 43.4, 45.2, 47, 48.7, 50.5, 52.2])
T_2 = T_2 - T_0

#i in 10^-11 ampere
I_1 = np.array([0.165, 0.21, 0.28, 0.38, 0.47, 0.59, 0.71, 0.9, 1.15, 1.45, 1.85, 2.4, 3.2, 4.1, 5.4, 7, 8.7, 10.5, 12.5, 14, 15, 12.5, 6.5, 5.4, 4, 3.2, 1.45, 0.45, 
                0.305, 0.26, 0.24, 0.23, 0.23, 0.24, 0.255, 0.275, 0.31, 0.33, 0.35, 0.36, 0.42, 0.45, 0.49, 0.54, 0.6, 0.66, 0.74, 0.81, 0.91, 
                1.05, 1.15, 1.30, 1.45, 1.65, 1.85, 2.05, 2.25, 2.45, 2.65, 2.85, 3, 3.1, 3.2, 3.2, 3.1, 2.95, 2.75, 2.55, 2.25, 1.95 ]) * 10**(-11)

I_2 = np.array([0.015, 0.015, -0.007, -0.01, -0.08, 0.015, 0.025, 0.03, 0.05, 0.06, 0.09, 0.125, 0.16, 0.22, 0.29, 0.35, 0.45, 0.6, 0.8, 1, 1.4, 1.8, 2.4, 3, 
                3.4, 4.5, 5.2, 5.7, 3, 3.2, 3.2, 1, 0.51, 0.4, 0.35, 0.32, 0.35, 0.38, 0.42, 0.46, 0.52, 0.59, 0.68, 0.78, 0.88, 1, 1.15,
                1.35, 1.55, 1.8, 2.1, 2.5, 2.95, 3.4, 3.6, 3.9, 4, 4, 3.9, 3.5, 3.1, 2.6, 2.2]) * 10**(-11)


#t in min
t_1 = np.linspace(0,69,70)
t_1[62] = 62.5

t_2 = np.arange(0, np.size(I_2), 1)

### Funktionen



def rel_abw(theo,a):
    c = (theo - a)/theo
    print(f"Relative Abweichung in Prozent: {noms(c) * 100 :.4f} \pm {stds(c) * 100 :.5f}\n")


def mittel(a,b,c):
    if (np.size(a) != np.size(b) or np.size(b) != np.size(c)):
        print("NICHT ALLE WERTE EINGETRAGEN")
        if(np.size(a)>np.size(b)):
            print("FEHLER IN ARRAY  b)")
        else:
            if(np.size(b)>np.size(c)):
                print("FEHLER IN ARRAY  c)")
            else:
                print("FEHLER IN ARRAY  a)")
    arr = unp.uarray(np.zeros(np.size(a)),np.zeros(np.size(a)))
    for i in range(0,np.size(a)):
        arr[i] = unc.ufloat(np.mean([a[i], b[i], c[i]]), np.std([a[i], b[i], c[i]])/ np.sqrt(3))
    return arr



def printer(a,b,c,d,name):
    print(f"### {name} ###")
    table1 ={'Messreihe 1': a, 'Messreihe 2': b,  'Messreihe 3': c, 'Messreihe 4': d }
    print("\n", tabulate(table1, tablefmt = "latex_raw"))    

def ploten(T, I, name):

    plt.figure()
    plt.plot(T, I, "x",  label = "Messwerte" )
    plt.fill_between(T[4:35], I[4:35], color="b", alpha=0.3)
    #plt.xscale('log')
    plt.rc('axes', labelsize= 12)
    plt.ylabel(r"I / pA")
    plt.xlabel(r"T / K")
    ##plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
    ##plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.savefig("build/plots/alles_" + name + ".pdf")

def ploten_mitunter(T, I, T_unter, I_unter, param,  name):

    T_fit = np.linspace(T[0],T[-1],500)

    plt.figure()
    plt.plot(T, I, ".",  label = "Messwerte" )
    plt.plot(T_unter, I_unter, "x",  label = "Untergrund" )
    plt.plot(T_fit, exp(T_fit, *param),  label = "Untergrundfit" )
    #plt.xscale('log')
    plt.rc('axes', labelsize= 12)
    plt.ylabel(r"I / pA")
    plt.xlabel(r"T / K")
    ##plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
    ##plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.savefig("build/plots/mitunter_" + name + ".pdf")

def ploten_ohneunter(T, I_rein, start, end, max, name):

    plt.figure()
    plt.plot(T, I_rein, "x",  label = "Messwerte" )
    plt.plot(T[start:end], I_rein[start:end], "x",  label = "Messwerte Integrale-Auswertung" )
    plt.plot(T[start:max+1], I_rein[start:max+1], "x",  label = "Messwerte Aprox" )
    plt.fill_between(T[start:end], I_rein[start:end], color="b", alpha=0.3)
    #plt.xscale('log')
    plt.rc('axes', labelsize= 12)
    plt.ylabel(r"I / pA")
    plt.xlabel(r"T / K")
    ##plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
    ##plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.savefig("build/plots/ohneunter_" + name + ".pdf")

def ploten_ascdesc(T_ascdesc, I_ascdesc, param, name):             #ascending-, descending-plot

    T_plot = np.linspace(T_ascdesc[0], T_ascdesc[-1], 500)

    plt.figure()
    plt.plot(T_ascdesc,np.log(I_ascdesc), "x",  label = "Messwerte" )
    plt.plot(T_plot, lin(T_plot, *param), label = "Ausgleichsgerade")
    #plt.yscale('log')
    plt.rc('axes', labelsize= 12)
    plt.ylabel(r"ln(I) / pA")
    plt.xlabel(r"T / K")
    ##plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
    ##plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.savefig("build/plots/" + name + ".pdf")

def ploten_tau(T_1, T_2):           


    plt.figure()
    plt.plot(T_1, exp(T_1, tau0_speicher[0], - W_speicher[0]/const.k), "gx",  label = r"Näherungsmethode $\Delta T = 1.5$K" )
    plt.plot(T_1, exp(T_1, tau0_speicher[1], - W_speicher[1]/const.k), "g.",  label = r"Integrationsmethode $\Delta T = 1.5$K"  )
    plt.plot(T_2, exp(T_2, tau0_speicher[2], - W_speicher[2]/const.k), "bx",  label = r"Näherungsmethode $\Delta T = 2$K"  )
    plt.plot(T_2, exp(T_2, tau0_speicher[3], - W_speicher[3]/const.k), "b.",  label = r"Integrationsmethode $\Delta T = 2$K"  )
    plt.yscale('log')
    plt.rc('axes', labelsize= 12)
    plt.ylabel(r"$\tau_0$ / s")
    plt.xlabel(r"T / K")
    ##plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
    ##plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.savefig("build/plots/tau_plot.pdf")

def heiz(T, name):
    a =(np.size(T)) -1
    a = int(a)
    diff = np.zeros(a)
    for i in range(0,a ):
        diff[i] = T[i+1] - T[i]

    b = unc.ufloat(np.mean(diff), np.mean(diff) / np.sqrt(a))
    print(f"\nHeizrate für die Messung {name}: {b}")
    return b

def exp(T, a, b):
    return a * np.exp((-b / T))

def lin(T, m, n):
    return m * T + n

def underground_fit(T_unter, I_unter):

    param, cov = curve_fit(exp, T_unter, I_unter)
    cov = np.sqrt(np.diag(cov))

    uparam = unp.uarray(param, cov)

    scale = 1            #um Werte vernünftig anzeigen zu können. Einheiten müssen noch geändert werden

    print(f"\nUntergrundfit: \na = {noms(uparam[0])* 10**scale:.4f} \pm {stds(uparam[0]) * 10**scale:.4f} * 10**{scale} A\t b = {noms(uparam[1]):.4f} \pm {stds(uparam[1]):.4f} K \n")

    return param                #nur param fürs plotten 

def tau_speichern(tau_0):
    global tau0_speicher

    if(tau0_speicher[0] == 0): 
        tau0_speicher[0] = tau_0
    elif(tau0_speicher[1] == 0): 
        tau0_speicher[1] = tau_0
    elif(tau0_speicher[2] == 0): 
        tau0_speicher[2] = tau_0
    elif(tau0_speicher[3] == 0): 
        tau0_speicher[3] = tau_0

def W_speichern(W):
    global W_speicher

    if(W_speicher[0] == 0): 
        W_speicher[0] = W
    elif(W_speicher[1] == 0): 
        W_speicher[1] = W
    elif(W_speicher[2] == 0): 
        W_speicher[2] = W
    elif(W_speicher[3] == 0): 
        W_speicher[3] = W

def tau_stuff(T, b, W):

    scale = 18

    tau_max = (const.k * T**2) / (b * W)
    tau_0 = tau_max * unp.exp(-W / (const.k * T)) * 10**(scale)
    
    print(f"\nRelaxationszeiten: \ntau_max = {noms(tau_max):.4f} \pm {stds(tau_max):.4f} s \ntau_0= ({noms(tau_0):.4f} \pm {stds(tau_0):.4f})e-{scale} s")

    tau_speichern(noms(tau_0))

def ascdesc_fit(T, I, b, argmax):


    param, cov = curve_fit(lin, 1/T, np.log(I))
    cov = np.sqrt(np.diag(cov))

    uparam = unp.uarray(param, cov)

    W = const.k * -1 * uparam[0]

    W_speichern(noms(W))

    W = W / const.e                  #now in eV

    print(f"\nAscDesc fit: \nm = {noms(uparam[0]):.4f} \pm {stds(uparam[0]):.4f} 1/T\t n = {noms(uparam[1]):.4f} \pm {stds(uparam[1]):.4f}  \n")
    print(f"Aktivierungsenergie: \nW = {noms(W):.4f} \pm {stds(W):.4f} eV")

    tau_stuff(T[argmax], b, W * const.e)         #T[-1] wiel  I dort maximal wird

    return param                #nur param fürs plotten

def slicer(arr, start, end, peak):

    arr_new = arr[:start]
    arr_new= np.append(arr_new, arr[end:peak])

    return arr_new

def ugly_main(T, I, start, end, peak,b, name):

    #Untergrund fitten

    T_unter = slicer(T, start, end, peak)
    I_unter = slicer(I, start, end, peak)
    print(name)
    param_unter = underground_fit(T_unter, I_unter)
    ploten_mitunter(T, I, T_unter, I_unter, noms(param_unter), name)

    #Untergrund abziehen und weitere Bereiche erkennen

    I_rein = np.zeros(np.size(I))

    for i in range(0,np.size(I)):
        I_rein[i] = I[i] - exp(T[i], *param_unter)

    
    max = np.argmax(I_rein)
    print(f"\nT_max = {T[max]:.4f} K\n")

    ploten_ohneunter(T, I_rein, start, end, max, name)    

    #aufsteigend auswerten
    print(f"\n### AUSWERTUNG Polarisation " + name + " ###\n")

    param_asc = ascdesc_fit(T[start:max+1],I[start:max+1], b, -1)   #-1, weil T[-1] mit I_max korrespondiert

    ploten_ascdesc(1/T[start:max+1], I_rein[start:max+1], param_asc, "asc_" + name)

    #Integrale Auswertung
    print(f"\n### AUSWERTUNG INTEGRAL " + name + " ###\n")
    I_int = integrate.cumtrapz(I_rein[start:end], T[start: end], initial=I_rein[start]) #Integral berechnen

    max = np.argmax(I_rein[start:end])
    param_int = ascdesc_fit(T[start:end], I_int/(I_rein[start:end]) , b, max)   #-max weil T[max] mit I_max korrespondiert
    ploten_ascdesc(1/T[start:end], I_int/(I_rein[start:end] ), param_int, "int_" + name)

    return I_rein                   #return für tabellen am ende


#############################Auswertung#####################################


print("\n########## AUSWERTUNG ###############\n\n")


#Willkür

start_1 = 4
end_1 = 28
T_peak_1 = 61

start_2 = 13
end_2 = 33
T_peak_2 = 56

tau0_speicher = np.zeros(4) #speicher um mit allen tau werten am ende zu plotten. ist kinda annoying und unnötig. 
W_speicher =np.zeros(4)

print("### mittlere Heizraten ###")

b_1 = heiz(T_1, "1.5 grad")
b_2 = heiz(T_2, "2 grad")

print("\n\n#### AUSWERTUNG 1.5°C ####")

I_rein_1 = ugly_main(T_1, I_1 , start_1, end_1, T_peak_1, b_1, "1.5grad")

print("\n\n#### AUSWERTUNG 2°C ####")

I_rein_2 = ugly_main(T_2, I_2, start_2, end_2, T_peak_2, b_2, "2grad")


print("\nFinal checkup tau_0: ", tau0_speicher,"")
print("Final checkup W: ", W_speicher,"\n")

ploten_tau(T_1, T_2)

###Tabellen

print("\n####### TABELLEN #########")

#printer(t_1, T_1, I_1* 10**(11), I_rein_1 * 10**(11), "Messung \delta T =1.5 Grad")

#printer(t_2, T_2, I_2* 10**(11), (I_rein_2 * 10**(11)), "Messung \delta T =2 Grad")

########Grafiken########

#ploten(T_1, I_1, "mess_1.5grad")
#ploten(T_2, I_2, "mess_2grad")

