import algorithms as A
import benchmark_functions as F 

functions = [F.Ackley, F.Alpine01, F.Alpine02, F.Bohachevsky, F.CosineMixture, F.DefCorrSpring, F.DixonPrice, F.Griewank, F.InvCosineWave, 
             F.Levy, F.Michalewicz_m1, F.Michalewicz_m10, F.Mishra07, F.Mishra11, F.Pathological, F.Rastrigin, F.Rosenbrock, F.Salomon, 
             F.Schwefel22, F.Schwefel26, F.SineEnvelope, F.StretchedVSine, F.StyblinskiTang, F.Trigonometric02, F.Vincent]


for f in functions:
    print(f'{f.__name__} : {f([40,70])}')
