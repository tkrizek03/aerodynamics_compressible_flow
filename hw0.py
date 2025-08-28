import math
import numpy as np
from rootSolvers import *
"""
Workspace for hw0

@author: Trey Krizek
"""
# Problem 1

def f1_res(m, ast_by_a, g):
    return ast_by_a - m*((g + 1)/(2 + (g-1)*m**2))**((g+1)/(2*g-2))

args = (0.6, 1.4)
root1a = rootSolvers.secant_solver(f1_res, *args, ic = 0.5)
root1b = rootSolvers.secant_solver(f1_res, *args, ic = 1.5)
print("Problem 1 (Secant Method)")
print(f"1a. {root1a}; 1b. {root1b}\n")

root1a = rootSolvers.bisection_solver(f1_res, *args, ivl = [0,1])
root1b = rootSolvers.bisection_solver(f1_res, *args, ivl = [1,10])
print("Problem 1 (Bisection Method)")
print(f"1a. {root1a}; 1b. {root1b}\n")

# Problem 2

def f2_res(sp, ast_by_a, g):
    return ast_by_a - (((2/(g-1))*(sp**((g-1)/g)-1))**.5) * (((g+1)/2)**(g/(g-1))/sp)**((g+1)/(2*g))

root2a = rootSolvers.secant_solver(f2_res, *args, ic = 1.5)
root2b = rootSolvers.secant_solver(f2_res, *args, ic = 2)
print("Problem 2 (Secant Method)")
print(f"2a. {root2a}; 2b. {root2b}\n")

root2a = rootSolvers.bisection_solver(f2_res, *args, ivl = [1, 1.893])
root2b = rootSolvers.bisection_solver(f2_res, *args, ivl = [1.893, 10])
print("Problem 2 (Bisection Method)")
print(f"2a. {root2a}; 2b. {root2b}\n")

# Problem 3

def f3_res(t, b, M1, g):
    lhs = np.tan(b) / np.tan(b - t)
    rhs = ((g+1) * M1**2 * np.sin(b)**2) / (2 + ((g-1) * M1**2 * np.sin(b)**2))
    return lhs - rhs

beta_a = np.deg2rad(30.935)

args3 = (beta_a, 4.5, 1.4)
root3a = np.rad2deg(rootSolvers.secant_solver(f3_res, *args3, ic = np.deg2rad(20)))
print("Problem 3 (Bisection Method)")
print(f"3a. {root3a}; ")

beta_a = np.deg2rad(84.269)

args3 = (beta_a, 4.5, 1.4)
root3b = np.rad2deg(rootSolvers.secant_solver(f3_res, *args3, ic = np.deg2rad(45)))
print(f"3b. {root3b}")

