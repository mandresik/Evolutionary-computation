import math as M



def Ackley(x):
    return -20 * M.exp(-0.2 * M.sqrt(sum(x[i]**2 for i in range(len(x))) / len(x))) - M.exp(sum(M.cos(2 * M.pi * x[i]) for i in range(len(x))) / len(x)) + 20 + M.exp(1)

def Alpine01(x):
    return sum(abs(x[i] * M.sin(x[i]) + 0.1 * x[i]) for i in range(len(x)))

def Alpine02(x):
    return M.prod(M.sqrt(x + 100) * M.sin(x + 100))

