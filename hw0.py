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
print(f"1a. {root1a:.5f}; 1b. {root1b:.5f}\n")

root1a = rootSolvers.bisection_solver(f1_res, *args, ivl = [0,1])
root1b = rootSolvers.bisection_solver(f1_res, *args, ivl = [1,10])
print("Problem 1 (Bisection Method)")
print(f"1a. {root1a:.5f}; 1b. {root1b:.5f}\n")

# Problem 2

def f2_res(sp, ast_by_a, g):
    return ast_by_a - (((2/(g-1))*(sp**((g-1)/g)-1))**.5) * (((g+1)/2)**(g/(g-1))/sp)**((g+1)/(2*g))

root2a = rootSolvers.secant_solver(f2_res, *args, ic = 1.5)
root2b = rootSolvers.secant_solver(f2_res, *args, ic = 2)
print("Problem 2 (Secant Method)")
print(f"2a. {root2a:.5f}; 2b. {root2b:.5f}\n")

root2a = rootSolvers.bisection_solver(f2_res, *args, ivl = [1, 1.893])
root2b = rootSolvers.bisection_solver(f2_res, *args, ivl = [1.893, 10])
print("Problem 2 (Bisection Method)")
print(f"2a. {root2a:.5f}; 2b. {root2b:.5f}\n")
