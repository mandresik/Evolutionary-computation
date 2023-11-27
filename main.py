import math as M



def Ackley(x):
    return -20 * M.exp(-0.2 * M.sqrt(sum(xi**2 for xi in x) / len(x))) - M.exp(sum(M.cos(2 * M.pi * xi) for xi in x) / len(x)) + 20 + M.exp(1)

def Alpine01(x): 
    return sum(abs(xi * M.sin(xi) + 0.1 * xi) for xi in x)

def Alpine02(x):
    return M.prod(M.sqrt(xi + 100) * M.sin(xi + 100) for xi in x)

