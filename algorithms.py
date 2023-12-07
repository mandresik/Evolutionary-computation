import numpy.random as rnd


# reflection in case some component of x is not in [lower_bound, upper_bound] interval
def reflect(x, lower_bound, upper_bound):
    # reflect x_i in x if x_i is out of bounds 
    for i in range(len(x)):
        if(x[i] < lower_bound): x[i] = 2 * lower_bound - x[i]
        if(x[i] > upper_bound): x[i] = 2 * upper_bound - x[i]
    return x

# mutation of type rand/1 
def mutation_rand_1(curr_index, population, F, lower_bound, upper_bound):
    # ind contains 3 random indices distinct of each other and curr_index
    ind = rnd.choice([i for i in range(len(population)) if i != curr_index], size = 3, replace = False)
    # mutant is then computed via 3 random distinct vectors (defined by ind) from population and parameter F
    mutant = [population[ind[0]][i] + F * (population[ind[1]][i] - population[ind[2]][i]) for i in range(len(population[0]))]
    # check whether all components of mutant are not out of bounds
    mutant = reflect(mutant, lower_bound, upper_bound)
    return mutant

# binomial crossover of parent and it's mutant, depending on constant CR
def binomial_crossover(parent, mutant, CR):
    D = len(parent)
    for i in range(D):
        # if random number from uniform distribution in [0,1] is <= CR or current index is randomly chosen amongst of all indices,  
        # then new component is taken from mutant, otherwise it is taken from parent
        if(rnd.rand() <= CR or i == rnd.randint(0, D)):
            parent[i] = mutant[i]
    return parent

# initializes population of size population_size, with vectors of size dimension, 
# where each dimension is in [lower_bound, upper bound] interval
def init_population(population_size, dimension, lower_bound, upper_bound):
    population = [[rnd.uniform(lower_bound, upper_bound) for _ in range(dimension)] for _ in range(population_size)]
    return population



# differential evolution
def DE_r1b(fitness, dimension, population_size, mx_generation, lower_bound, upper_bound, F, CR):
    # initialization of population
    population = init_population(population_size, dimension, lower_bound, upper_bound)

    # initialization of best x and it's fitness value
    x_best = population[0]
    fx_best = fitness(x_best)

    for _ in range(mx_generation):

        for i in range(population_size):
            # mutation
            mutant = mutation_rand_1(i, population, F, lower_bound, upper_bound)
            # crossover
            cross = binomial_crossover(population[i], mutant, CR)
            fitness_cross = fitness(cross)
            # selection
            if(fitness_cross <= fitness(population[i])):
                population[i] = cross
                if(fitness_cross <= fx_best):
                    x_best = cross
                    fx_best = fitness_cross

    
    return fx_best


