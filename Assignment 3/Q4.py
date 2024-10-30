# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Bandgap
Eg = 1.51

# Design function to solve for the Bandgap
def EgComp (x):
    return 1.424  + 1.266*x + 0.266*x**2 - Eg

# Solve for Root
sol = fsolve(EgComp, 0.2)

# Print Answer
print("\n")
print(f"X = {sol[0]}")
print("\n")