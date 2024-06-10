# Evolutionary computation
This is a school project that compares evolutionary algorithms using benchmark functions. This comparison is described in the attached pdf file as follows:
* 25 benchmark functions are introduced (formulas, 2D and 3D graphs).
* Every algorithm runs 30 times on each test function, initial population is chosen randomly on the interval $\left\langle -100,100 \right\rangle$ and all individuals stays within these bounds using reflection method.
Global minimum of these 30 runs is averaged and listed in a table.
* Next table shows ranking, meaning which algorithm found better results for each function. We compare the average rank of all algoritms and mark 5 functions with the biggest differences in the average ranks. We also try to figure out why this happens. 
* These results and rankings are calculated in dimensions 2, 10 and 30.
* Lastly, we use Friedmann rank test to find out whether the ranking of these algoritms is consisted in the investgated dimensions.

## Benchmark functions
benchmark_function folder contains matlab scripts that were used for plotting the graphs to visualize each function's behaviour. In benchmark_functions.py, these functions are implemented for function evaluations. 

## Algorithms
Algorithms are implemented in the algorithms.py and algorithms_fes.py. These scripts are almost identical with one major difference. Stopping condition in algoritms.py is finishing iteration/migration of all individuals,
depending on each algoritm's behaviour. Stopping condition in algorithms_fes.py is the count of function evaluations (FES). Implemented algorithms are:
* DE_rand_1_bin - differential evolution with rand/1 mutation and binomial crossover,
* DE_best_1_bin - differential evolution with best/1 mutation and binomial crossover,
* PSO - partical swarm optimization algorithm,
* SOMA_all_to_one - self organizing migrating algorithm with all-to-one migration,
* SOMA_all_to_all - self organizing migrating algorithm with all-to-all migration.

## Results
All results are saved in the results folder, together with the friedmann rank test script. Running this project and saving the results (as described earlier - 30 runs of all 5 algorithms on 25 benchmark functions) 
is done in the main.py script.
