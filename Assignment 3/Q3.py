#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Initial Variables
Na = 10**15 # cm^-3
Nd = 10**17 # cm^-3
B = 4*10**(-16) #m^3/s
A = 1 # mm^2
T = 300 # K
V1 = 0.70 # V
V2 = 0.90 # V
mue = 6000 # cm^2/Vs
muh = 100 # cm^2/Vs
kB = 1.38*10**(-23) # J/K
e = 1.602*10**(-19) # C
ni = 3*10**7 # cm^-3
cm2tom2 = 10**(-4)
cm3tom3 = 10**6
eps0 = 8.85*10**(-12) # F/m
epsr = 12.6

#Calculate Lifetimes
taue = 1/(B*(Na)*100**3)
tauh = 1/(B*(Nd)*100**3)

print("\n")
print(f"Electron Lifetime = {taue} s")
print(f"Hole Lifetime = {tauh} s")

# Calculate Diffusions
De = (kB*T*mue*cm2tom2)/e
Dh = (kB*T*muh*cm2tom2)/e

print("\n")
print(f"Electron Diffusions = {De} m^2/s")
print(f"Hole Diffusion = {Dh} m^2/s")


# Calculate Lifetimes in terms of Diffusions
Le = np.sqrt(De*taue)
Lh = np.sqrt(Dh*tauh)

print("\n")
print(f"Electron Diffusion Length = {Le} m")
print(f"Hole Diffusion Length = {Lh} m")

# Calculate Diffusion Currents
V = np.array([V1,V2])

J = (((e*De)/(Le*Na*cm3tom3))+((e*Dh)/(Lh*Nd*cm3tom3))) * (ni* cm3tom3)**2 * (np.exp((e*V)/(kB*T))-1)

print ("\n")
print(f"Diffusion Current {V[0]} V = {J[0]} A/m^2")
print(f"Diffusion Currents {V[1]} V = {J[1]} A/m^2")

J = J / (1000)**2

print ("\n")
print(f"Diffusion Current {V[0]} V = {J[0]} A")
print(f"Diffusion Currents {V[1]} V = {J[1]} A")

#
# Recombination Currents
#

# Calculate Voltage Bias
V0 = (kB * T / e)*np.log((Na * Nd)/ni**2)

print ("\n")
print(f"Voltage Bias = {V0} V")

# Calculate Depletion Widths
W = np.sqrt((2*epsr*eps0*cm3tom3*(Na + Nd)*(V0 -V))/(e*Na*cm3tom3*Nd*cm3tom3))

print ("\n")
print(f"Depletion Width {V[0]} V = {W[0]} m")
print(f"Depletion Width {V[1]} V = {W[1]} m")

# Calculate Depletion Widths for N and P

Wn = W * 1/(Nd/Na + 1)
Wp = W * 1/(Na/Nd + 1)

#Wn = W * (Nd/(Na + Nd))
#Wp = W * (Na/(Na + Nd))

print ("\n")
print(f"Depletion Width N {V[0]} V = {Wn[0]} m")
print(f"Depletion Width N {V[1]} V = {Wn[1]} m")

print ("\n")
print(f"Depletion Width P {V[0]} V = {Wp[0]} m")
print(f"Depletion Width P {V[1]} V = {Wp[1]} m")

# Calculate Recombination Currents

Jro = ((e*ni*cm3tom3)/2) * (Wp/taue + Wn/tauh) * np.exp((e*V)/(2*kB*T))

print ("\n")
print(f"Recombination Current {V[0]} V = {J[0]} A/m^2")
print(f"Recombination Currents {V[1]} V = {J[1]} A/m^2")

Jro = Jro / (1000)**2

print ("\n")
print(f"Recombination Current {V[0]} V = {J[0]} A")
print(f"Recombination Currents {V[1]} V = {J[1]} A")

# Determine if Diffusion or Recombination Dominant
print ("\n")
for i in range(2):
    if (J[i] > Jro[i]):
        print(f"Diffusion Dominant at {V[i]} V")
    else:
        print(f"Recombination Dominant at {V[i]} V")


