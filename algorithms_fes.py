import numpy.random as rnd

"""
---------------------------------- algorithms_fes.py ----------------------------------

In algorithms_fes.py, for all algorithms, stopping condition is count of function evaluations FES. 
With each algorithms's behaviour, this may result in an uncomplete last migration (not all individuals migrated).
Completing last migration in each algorithm is ensured in algorithms.py.

Implemented algorithms: 
    DE_rand_1_bin       differential evolution with rand/1 mutation and binomial crossover
    DE_best_1_bin       differential evolution with best/1 mutation and binomial crossover
    PSO                 partical swarm optimization algorithm
    SOMA_all_to_one     self organizing migrating algorithm with all-to-one migration
    SOMA_all_to_all     self organizing migrating algorithm with all-to-all migration

Time complexities: 
    All algorithms has the same time complexity    O( FES ).

"""


# reflection in case some component of x is not in [lower_bound, upper_bound] interval
def reflect(x, lower_bound, upper_bound):
    # reflect x_i in x if x_i is out of bounds 
    for i in range(len(x)):
        if(x[i] < lower_bound): x[i] = 2 * lower_bound - x[i]
        if(x[i] > upper_bound): x[i] = 2 * upper_bound - x[i]
    # if x_i was too small or too large and is still out of bounds, repeat reflection until it is within bounds
    if(all(xi >= lower_bound and xi <= upper_bound for xi in x)): return x
    else: return reflect(x, lower_bound, upper_bound)


# mutation of type rand/1 
def mutation_rand_1(curr_index, population, F, lower_bound, upper_bound):
    # ind contains 3 random indices distinct of each other and curr_index
    ind = rnd.choice([i for i in range(len(population)) if i != curr_index], size = 3, replace = False)
    # mutant is then computed via 3 random distinct indiiduals (defined by ind) from population and parameter F
    mutant = [population[ind[0]][i] + F * (population[ind[1]][i] - population[ind[2]][i]) for i in range(len(population[0]))]
    # check whether all components of mutant are not out of bounds
    mutant = reflect(mutant, lower_bound, upper_bound)
    return mutant


# mutation of type best/1
def mutation_best_1(best_index, population, F, lower_bound, upper_bound):
    # ind contains 2 random indices distinct from each other and best_index
    ind = rnd.choice([i for i in range(len(population)) if i != best_index], size = 2, replace = False)
    # mutant is then computed via best individual in the population and 2 other random individuals and parameter F
    mutant = [population[best_index][i] + F * (population[ind[0]][i] - population[ind[1]][i]) for i in range(len(population[0]))]
    # check whether all components are not out of bounds
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
    return [[rnd.uniform(lower_bound, upper_bound) for _ in range(dimension)] for _ in range(population_size)]


# initializes velocity for each component of each particle in range [v_min, v_max]
def init_velocity(population_size, dimension, v_min, v_max):
    return [[rnd.uniform(v_min, v_max) for _ in range(dimension)] for _ in range(population_size)]


# calculates velocity in PSO algorithm
def calc_velocity(velocity, particle, p_best, g_best, w, c1, c2):
    return [w * velocity[j] + c1 * rnd.rand() * (p_best[j] - particle[j]) + c2 * rnd.rand() * (g_best[j] - particle[j]) for j in range(len(particle))]



# differential evolution with rand/1 mutation and binomial crossover
def DE_rand_1_bin(fitness, dimension, population_size, FES, lower_bound, upper_bound, F, CR):
    # initialization of population and it's ftiness values
    population = init_population(population_size, dimension, lower_bound, upper_bound)
    fitness_population = [fitness(individual) for individual in population]

    # keeping track of best fitness value found
    fx_best = fitness_population[0]

    fes = 0
    while(True):

        for i in range(population_size):
            # mutation
            mutant = mutation_rand_1(i, population, F, lower_bound, upper_bound)
            # crossover
            cross = binomial_crossover(population[i], mutant, CR)
            fitness_cross = fitness(cross)
            # selection
            if(fitness_cross <= fitness_population[i]):
                population[i] = cross
                fitness_population[i] = fitness_cross
                if(fitness_cross <= fx_best):
                    fx_best = fitness_cross

            fes += 1
            if(fes == FES): return fx_best



# differential evolution with best/1 mutation and binomial crossover
def DE_best_1_bin(fitness, dimension, population_size, FES, lower_bound, upper_bound, F, CR):
    # initialization of population and it's fitness values
    population = init_population(population_size, dimension, lower_bound, upper_bound)
    fitness_population = [fitness(individual) for individual in population]

    # initialization of index of best individual and keeping track of best fitness value found
    i_best = 0
    fx_best = fitness_population[0]

    fes = 0
    while(True):

        for i in range(population_size):
            # mutation
            mutant = mutation_best_1(i_best, population, F, lower_bound, upper_bound)
            # crossover
            cross = binomial_crossover(population[i], mutant, CR)
            fitness_cross = fitness(cross)
            # selection
            if(fitness_cross <= fitness_population[i]):
                population[i] = cross
                fitness_population[i] = fitness_cross
                if(fitness_cross <= fx_best):
                    i_best = i
                    fx_best = fitness_cross

            fes += 1
            if(fes == FES): return fx_best



# partical swarm optimization
def PSO(fitness, dimension, population_size, FES, lower_bound, upper_bound, w, c1, c2):
    # initialization of particles
    particles = init_population(population_size, dimension, lower_bound, upper_bound)
    # every particle's found best position and it's fitness
    particles_best = particles
    fitness_p_best = [fitness(particle) for particle in particles_best]
    # global best, particle with the smallest fitness value
    global_best = min(particles_best, key = lambda x : fitness(x))
    fitness_g_best = fitness(global_best)
    # velocities of particles, initially set to zero
    velocity = init_velocity(population_size, dimension, 0, 0)

    fes = 0
    while(True):

        for i in range(population_size):
            # calculation of new velocity and new position
            new_velocity = calc_velocity(velocity[i], particles[i], particles_best[i], global_best, w, c1, c2)
            new_position = reflect([particles[i][j] + new_velocity[j] for j in range(dimension)], lower_bound, upper_bound)
            # compare fitness of new position with fitness of particle_best and possibly global_best
            fitness_new_pos = fitness(new_position)
            if(fitness_new_pos < fitness_p_best[i]):
                particles_best[i] = new_position
                fitness_p_best[i] = fitness_new_pos
                if(fitness_new_pos < fitness_g_best):
                    global_best = new_position
                    fitness_g_best = fitness_new_pos
            # update new particle's velocity and position
            velocity[i] = new_velocity
            particles[i] = new_position

            fes += 1
            if(fes == FES): return fitness_g_best



# self organizing migrating algorithm with all-to-one migration
def SOMA_all_to_one(fitness, dimension, population_size, FES, lower_bound, upper_bound, step_size, path_length, PRT):
    # initialization of population and it's fitness values
    population = init_population(population_size, dimension, lower_bound, upper_bound)
    fitness_population = [fitness(individual) for individual in population]
    # fx_best keeps the best fitness found 
    fx_best = fitness_population[0]

    fes = 0
    while(True):
        # individual with smallest fitness value is chosen as leader
        leader = min(population, key = lambda x : fitness(x))
        leader_i = population.index(leader)
        fx_best = fitness(leader)

        for i in range(population_size):
            # each individual (except for leader) moves towards leader
            if(i != leader_i):
                t = 0
                # best_on_trajectory is individual with best fitness value on trajectory that will be saved for new population
                best_on_trajectory = population[i]
                fitness_best_on_traj = fitness_population[i]
                while(t <= path_length):
                    # calculation of individual on the trajectory
                    prt_vector = [float(rnd.rand() < PRT) for _ in range(dimension)]
                    new_individual = reflect([population[i][j] + (leader[j] - population[i][j]) * t * prt_vector[j] for j in range(dimension)], lower_bound, upper_bound)
                    fitness_new_individual = fitness(new_individual)
                    # keeping track of best found on the trajectory
                    if(fitness_new_individual < fitness_best_on_traj):
                        best_on_trajectory = new_individual
                        fitness_best_on_traj = fitness_new_individual
                        # keeping track of the best fitness found
                        if(fitness_best_on_traj < fx_best): 
                            fx_best = fitness_best_on_traj

                    t += step_size
                    fes += 1
                    if(fes == FES): return fx_best

                # saving best on trajectory for new population
                population[i] = best_on_trajectory
                fitness_population[i] = fitness_best_on_traj



# self organizing migrating algorithm with all-to-all migration
def SOMA_all_to_all(fitness, dimension, population_size, FES, lower_bound, upper_bound, step_size, path_length, PRT):
    # initialization of population and it's fitness values
    population = init_population(population_size, dimension, lower_bound, upper_bound)
    fitness_population = [fitness(individual) for individual in population]
    # fx_best keeps the best fitness found 
    fx_best = fitness_population[0]

    fes = 0
    while(True): 
        # saving new population for upcoming migration
        new_population = [[0 for _ in range(dimension)] for _ in range(population_size)]
        new_fitness_population = [0 for _ in range(population_size)]

        # trajectories starting in population[s] and ending in population[e]
        for s in range(population_size): 
            # keeping track of the best individual starting in population[s]
            best_from_s = population[s]
            fitness_best_from_s = fitness_population[s]
            # investigating all trajectories from population[s]
            for e in range(population_size):
                if(s != e):
                    t = 0
                    while(t <= path_length):
                        prt_vector = [float(rnd.rand() < PRT) for _ in range(dimension)]
                        new_individual = reflect([population[s][j] + (population[e][j] - population[s][j]) * t * prt_vector[j] for j in range(dimension)], lower_bound, upper_bound)
                        fitness_new_individual = fitness(new_individual)
                        # keeping track of best found from population[s]
                        if(fitness_new_individual < fitness_best_from_s):
                            best_from_s = new_individual
                            fitness_best_from_s = fitness_new_individual
                            # keeping track of the best fitness found
                            if(fitness_best_from_s < fx_best): 
                                fx_best = fitness_best_from_s

                        t += step_size
                        fes += 1
                        if(fes == FES): return fx_best

            # saving best individual found on trajectory from population[s]
            new_population[s] = best_from_s
            new_fitness_population[s] = fitness_best_from_s

        population = new_population
        fitness_population = new_fitness_population

