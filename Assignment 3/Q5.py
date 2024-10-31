#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define Constants
h = 6.626*10**(-34) 
me = 9.109*10**(-31)
meStar = 0.067*me
Dy = 2 *10**(-6)
Dz = 2 *10**(-6)
d = 10 * 10**(-9)


def nTerm (n):
    return (h**2*n**2)/(8*meStar*d**2)

def nyTerm (ny):
    return (h**2*ny**2)/(8*meStar*Dy**2)

def nzTerm (nz):
    return (h**2*nz**2)/(8*meStar*Dz**2)

MinEnergy = nTerm(1) + nyTerm(1) + nzTerm(1)

print("\n")
print(f"Min Energy = {MinEnergy}")
print(f"N Term = {nTerm(1)}")
print(f"Ny Term = {nyTerm(1)}")
print(f"Nz Term = {nzTerm(1)}")

print(f"N Term % = {nTerm(1)/MinEnergy*100}")
print(f"Ny Term % = {nyTerm(1)/MinEnergy*100}")
print(f"Nz Term % = {nzTerm(1)/MinEnergy*100}")

delta = (h**2)/(8*meStar*Dy**2)

print(f"Delta = {delta}")
