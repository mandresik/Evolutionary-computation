import math as M


def Ackley(x):
    return -20 * M.exp(-0.2 * M.sqrt(sum(xi**2 for xi in x) / len(x))) - M.exp(sum(M.cos(2 * M.pi * xi) for xi in x) / len(x)) + 20 + M.exp(1)

def Alpine01(x):
    return sum(abs(xi * M.sin(xi) + 0.1 * xi) for xi in x)

def Alpine02(x):
    return M.prod(M.sqrt(xi + 100) * M.sin(xi + 100) for xi in x)

def Bohachevsky(x): 
    return sum(x[i]**2 + 2 * x[i + 1]**2 - 0.3 * M.cos(3 * M.pi * x[i]) - 0.4 * M.cos(4 * M.pi * x[i + 1]) + 0.7 for i in range(len(x) - 1))

def CosineMixture(x):
    return -0.1 * sum(M.cos(5 * M.pi * xi) for xi in x) + sum(xi**2 for xi in x)

def DefCorrSpring(x, a = 5, K = 5):
    return 0.1 * sum((xi - a)**2 - M.cos(K * M.sqrt(sum((xi - a)**2 for xi in x))) for xi in x)

def DixonPrice(x): 
    return (x[0] - 1)**2 + sum((i + 2) * (2 * x[i + 1]**2 - x[i])**2 for i in range(len(x) - 1))

def Griewank(x):
    return 1 + sum(xi**2 for xi in x) / 4000 - M.prod(M.cos(x[i] / M.sqrt(i + 1)) for i in range(len(x)))

def InvCosineWave(x):
    w = [x[i]**2 + x[i + 1]**2 + 0.5 * x[i] * x[i + 1] for i in range(len(x) - 1)]
    return -sum(M.exp(-wi / 8) * M.cos(4 * M.sqrt(wi)) for wi in w)

def Levy(x): 
    w = [1 + (xi - 1) / 4 for xi in x]
    return M.sin(M.pi * w[0])**2 + sum((w[i] - 1)**2 * (1 + 10 * M.sin(M.pi * w[i] + 1)**2) for i in range(len(x) - 1)) + (w[-1] - 1)**2 * (1 + M.sin(2 * M.pi * w[-1])**2)

def Michalewicz(x, m):
    return -sum(M.sin(x[i]) * M.sin((i + 1) * x[i]**2 / M.pi)**(2 * m) for i in range(len(x)))

def Michalewicz_m1(x):
    return Michalewicz(x, 1)

def Michalewicz_m10(x):
    return Michalewicz(x, 10)

# f is precalculated value of factorial, f = (len(x))!
def Mishra07(x, f): 
    return (M.prod(xi for xi in x) - f)**2

def Mishra11(x):
    return (sum(abs(xi) for xi in x) / len(x) - M.prod(abs(xi) for xi in x)**(1 / len(x)))**2

def Pathological(x): 
    return sum(0.5 + (M.sin(M.sqrt(100 * x[i]**2 + x[i + 1]**2))**2 - 0.5) / (1 + 0.001 * (x[i]**2 - 2 * x[i] * x[i + 1] + x[i + 1]**2)**2) for i in range(len(x) - 1))

