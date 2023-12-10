import numpy.random as rnd


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


def calc_velocity(velocity, particle, p_best, g_best, w, c1, c2):
    return [w * velocity[j] + c1 * rnd.rand() * (p_best[j] - particle[j]) + c2 * rnd.rand() * (g_best[j] - particle[j]) for j in range(len(particle))]



# differential evolution with rand/1 mutation and binomial crossover
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



# differential evolution with best/1 mutation and binomial crossover
def DE_b1b(fitness, dimension, population_size, mx_generation, lower_bound, upper_bound, F, CR):
    # initialization of population
    population = init_population(population_size, dimension, lower_bound, upper_bound)

    # initialization of best x, it's index in popupation and it's fitness value
    i_best = 0
    x_best = population[i_best]
    fx_best = fitness(x_best)

    for _ in range(mx_generation):

        for i in range(population_size):
            # mutation
            mutant = mutation_best_1(i_best, population, F, lower_bound, upper_bound)
            # crossover
            cross = binomial_crossover(population[i], mutant, CR)
            fitness_cross = fitness(cross)
            # selection
            if(fitness_cross <= fitness(population[i])):
                population[i] = cross
                if(fitness_cross <= fx_best):
                    i_best = i
                    x_best = cross
                    fx_best = fitness_cross

    return fx_best



# partical swarm optimization
def PSO(fitness, dimension, population_size, mx_generation, lower_bound, upper_bound, w, c1, c2):
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

    for _ in range(mx_generation):

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

    return fitness_g_best



# SOMA
def SOMA():
    return 0

