"""
Nonlinear root solver class for AERE 3110

@author: Trey Krizek
"""

class rootSolvers():
    
    def bisection_solver(f, *args, ivl, tol=1e-9, max_iter=500):
        a = ivl[0]
        b = ivl[1]
        
        if f(a, *args) * f(b, *args) >=0:
            raise ValueError("The function must have opposite signs at a and b.")
            
        for i in range(max_iter):
            c = (a + b) / 2
            fc = f(c, *args)
            if abs(fc) < tol:
                return c
            if f(a, *args) * fc < 0:
                b = c
            else:
                a = c
        raise ValueError("Bisection solver did not converge within max_iter iterations.")
        
    def secant_solver(f, *args, ic, tol=1e-9, max_iter=500):
        x0 = ic - 1e-2
        x1 = ic + 1e-2
        
        for i in range(max_iter):
            fx0 = f(x0, *args)
            fx1 = f(x1, *args)
            dx = (x1 - x0) * fx1 / (fx1 - fx0)
            x0 = x1
            x1 -= 0.2 * dx
            if abs(dx) < tol:
                return x1
        raise ValueError("Secant solver did not converge within max_iter iterations.")
        
        
        

