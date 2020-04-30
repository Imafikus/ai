import random

PATH_LENGTH = 10
PREDEFINED_PATH = '1110101011'

WALK_RIGHT = '1'
JUMP_RIGHT = '0'

MAX_POSSIBLE_FITNESS = 10

POPULATION_SIZE = 10
CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.05

class Chromosome:
    def __init__(self, content, fitness):
        self.content = content
        self.fitness = fitness
    
    def __str__(self):
        return 'Content:' + str(self.content) + '; Fitness:' + str(self.fitness)


def generate_initial_content():
    possible_values = ['1', '0']
    content = ''
    for i in range(0, PATH_LENGTH):
        content += random.choice(possible_values)
    
    return content

def calculate_fitness(content):
    fitness = 0

    for i in range(0, PATH_LENGTH):
        if content[i] == PREDEFINED_PATH[i]:
            fitness += 1
        
        else:
            break

    return fitness

def generate_initial_population():
    population = []

    for i in range(0, POPULATION_SIZE):
        content = generate_initial_content()
        fitness = calculate_fitness(content)
        population.append(Chromosome(content, fitness))

    return population

def selection(population):
    random_idxs = random.sample(range(0, POPULATION_SIZE), 3)
    current_best_chromosome = None

    for idx in random_idxs:
        if current_best_chromosome == None or current_best_chromosome.fitness < population[idx].fitness:
            current_best_chromosome = population[idx]
    
    return current_best_chromosome.content


def crossover(parent1, parent2):
    child1 = ''
    

    for i in range(PATH_LENGTH):
        if random.random() < CROSSOVER_RATE:
            child1 += parent1[i]
        else:
            child1 += parent2[i]
    
    return child1

def mutation(chromosome):
    for i in range(0, PATH_LENGTH):
        if random.random() < MUTATION_RATE:
            if chromosome[i] == WALK_RIGHT:
                chromosome = list(chromosome)
                chromosome[i] = JUMP_RIGHT
                chromosome = ''.join(chromosome)
            else:
                chromosome = list(chromosome)
                chromosome[i] = WALK_RIGHT
                chromosome = ''.join(chromosome)

    return chromosome


def get_best_chromosome(population):
    population.sort(key=lambda x: x.fitness)
    return population[-1]


def main():
    population = generate_initial_population()

    iteration = 0
    while True:
        print('Iteration: ',iteration)
        current_best = get_best_chromosome(population)
        if current_best.fitness == MAX_POSSIBLE_FITNESS:
            print('Solution found: ', current_best.__str__())
            break
        else:
            print('Current best: ', current_best.__str__())

        new_population = []
        for i in range(0, POPULATION_SIZE // 2):
            new_population.append(selection(population))

        for i in range(0, POPULATION_SIZE // 2):
            new_population.append(crossover(random.choice(new_population), random.choice(new_population)))

        for p in new_population:
            p = mutation(p)

        population = []
        for p in new_population:
            fitness = calculate_fitness(p)
            population.append(Chromosome(p, fitness))

    


if __name__ == "__main__":
    main()