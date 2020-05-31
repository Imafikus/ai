import random


PREFEDINED_PATH = '111010101100101'
POPULATION_SIZE = 60

GROUND = '1'
NO_GROUND = '0'

GO_RIGHT = '1'
JUMP_RIGHT = '0'

MUTATION_RATE = 0.05

class SuperMario:
    
    def __init__(self):
        self.population = self.generate_initial_population()


    def tournament_selection(self, t_size=5):
        tournament_population = random.sample(self.population, t_size)

        best_chromosome = None
        best_score = 0

        for chromosome in tournament_population:
            if self.get_score(chromosome) >= best_score:
                best_chromosome = chromosome
                best_score = self.get_score(chromosome)

        return best_chromosome

    def get_score(self, chromosome):
        score = 0
        for i, move in enumerate(chromosome):
            if move == GO_RIGHT and PREFEDINED_PATH[i] == NO_GROUND:
                break
            score += 1
        
        return score


    def crossover(self, chrom1, chrom2):
        pivot = random.randint(1, len(PREFEDINED_PATH))

        new_chrom1 = chrom1[:pivot] + chrom2[pivot:]
        new_chrom2 = chrom2[:pivot] + chrom1[pivot:]

        return new_chrom1, new_chrom2

    def mutation(self, population):

        for i, chromosome in enumerate(population):
            mutated_chromosome = ''
            for move in chromosome:
                if random.random() <= MUTATION_RATE:
                    if move == GO_RIGHT:
                        mutated_chromosome += JUMP_RIGHT
                    else:
                        mutated_chromosome += GO_RIGHT
                else:
                    mutated_chromosome += move
            population[i] = mutated_chromosome
        return population

    def get_best(self):

        best_chromosome = None
        best_score = 0

        for chromosome in self.population:
            if self.get_score(chromosome) >= best_score:
                best_chromosome = chromosome
                best_score = self.get_score(chromosome)

        return best_chromosome, best_score

    def generate_initial_population(self):
        population = []
        for i in range (0, POPULATION_SIZE):
            single_chromosome = ""
            for j in range(0, len(PREFEDINED_PATH)):
                single_chromosome += random.choice(['1', '0'])
            population.append(single_chromosome)
        return population


    def run(self):

        it = 0
        while True:

            print(f'Current iteration: {it}')
            current_best, score = self.get_best()
            if score == len(PREFEDINED_PATH):
                print('SCORE: ', score)
                print('SOLUTION FOUND: ', current_best)
                exit()
                
            else:
                print('CURRENT_BEST_SCORE: ', score)



            new_population = []

            for i in range(0, POPULATION_SIZE // 2):
                new_population.append(self.tournament_selection())
            
            for i in range(0, POPULATION_SIZE // 2):
                new_c1, new_c2 = self.crossover(new_population[i], new_population[i + 1])
                new_population.append(new_c1)
            
            new_population = self.mutation(new_population)

            self.population = new_population
            it += 1



if __name__ == "__main__":
    SuperMario().run()