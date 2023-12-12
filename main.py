import algorithms_fes as A
import benchmark_functions as F 
import pandas 
from scipy.stats import rankdata

# --------------------------------
# formatting small and large numbers for better overview
def format_number(num):
    if(num == 0):
        return float(0)
    elif abs(num) < 1e-3 or abs(num) > 1e6:
        return f"{num:1.4e}"
    elif(abs(num) > 1e3):
        return f"{num:.2f}"
    else:
        return f"{num:.5f}"


# --------------------------------
# BENCHMARK FUNCTIONS

functions = [F.Ackley, F.Alpine01, F.Alpine02, F.Bohachevsky, F.CosineMixture, F.DefCorrSpring, F.DixonPrice, F.Griewank, F.InvCosineWave, 
             F.Levy, F.Michalewicz_m1, F.Michalewicz_m10, F.Mishra07, F.Mishra11, F.Pathological, F.Rastrigin, F.Rosenbrock, F.Salomon, 
             F.Schwefel22, F.Schwefel26, F.SineEnvelope, F.StretchedVSine, F.StyblinskiTang, F.Trigonometric02, F.Vincent]


# --------------------------------
# PARAMETERS SETUP

# for DE
f = 0.8
cr = 0.9
# for PSO
c = 1.49618
w = 0.7298
# for SOMA
step_size = 0.11
path_length = 3
prt = 0.7
# general
lower_bound = -100
upper_bound = 100
dimension = 2
population_size = 10
FES = 2000 * dimension


# --------------------------------
# CALCULATION of results and ranks

repetitions = 30

# both RESULTS and RANKS are 2D lists with benchmark functions as rows and algorithms as columns
RESULTS = [[0 for _ in range(5)] for _ in range(25)]
RANKS = [[0 for _ in range(5)] for _ in range(25)]

for i, fun in enumerate(functions):

    # results of algorithms for each function, as an average in repetitions
    result_i = [0 for _ in range(5)]
    for _ in range(repetitions):

        result_i[0] += A.DE_rand_1_bin(fun, dimension, population_size, FES, lower_bound, upper_bound, f, cr)
        result_i[1] += A.DE_best_1_bin(fun, dimension, population_size, FES, lower_bound, upper_bound, f, cr)
        result_i[2] += A.PSO(fun, dimension, population_size, FES, lower_bound, upper_bound, w, c, c)
        result_i[3] += A.SOMA_all_to_one(fun, dimension, population_size, FES, lower_bound, upper_bound, step_size, path_length, prt)
        result_i[4] += A.SOMA_all_to_all(fun, dimension, population_size, FES, lower_bound, upper_bound, step_size, path_length, prt)

    # average fx_best in repetitions
    for j in range(5): 
        result_i[j] /= repetitions 
    result_i = [format_number(ri) for ri in result_i]
    # ranks of results 
    ranks_i = rankdata(result_i)
    ranks_i = [int(ri) for ri in ranks_i]

    # saving each row 
    RESULTS[i] = result_i
    RANKS[i] = ranks_i


# --------------------------------
# EXPORT results and ranks as .csv files

t_results = pandas.DataFrame(RESULTS)
t_results.index = [str(fun.__name__) for fun in functions]
t_results.columns = ["DE_rand_1_bin", "DE_best_1_bin", "PSO", "SOMA_all_to_one", "SOMA_all_to_all"]
t_results.to_csv(f'Results_{dimension}D.csv')

t_ranks = pandas.DataFrame(RANKS)
t_ranks.index = [str(fun.__name__) for fun in functions]
t_ranks.columns = ["DE_rand_1_bin", "DE_best_1_bin", "PSO", "SOMA_all_to_one", "SOMA_all_to_all"]
t_ranks.to_csv(f'Ranks_{dimension}D.csv')