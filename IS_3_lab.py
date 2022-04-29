import random
MIN, MAX = -5.12, 5.11
AMOUNT_OF_POPULATION =50
L = 0.5  # параметр для селекции
PC = 0.9  # параметр для скрещивания
alpha = 0.5  # параметр альфа для кроссинговера
PM = 1 / AMOUNT_OF_POPULATION  # вероятность мутации
 
#Фитнес-функция
def fitness_function(individual):
    return - (individual) * (individual) + 4
#Функция скрещивания
def truncation_selection(population_fitness, AMOUNT_OF_POPULATION, L):
    chosen = []
    for i in range(round(AMOUNT_OF_POPULATION * L)):
        chosen.append(population_fitness[i][1])
    return (chosen)
 
 
 
def rand():
    return (round(random.uniform(0, 1)))
 
#Функция blx_a кроссинговера
def BLX_a(g1, g2, new_population, a):
    cmin = min(g1, g2)
    cmax = max(g1, g2)
    delta = cmax - cmin
    for i in range(2):
        new_population.append(random.uniform(cmin - a * delta, cmax + a * delta))
# Создание начальной популяции
initial_population = []
print("Initial array")
for i in range(AMOUNT_OF_POPULATION):
    initial_population.append(random.uniform(MIN, MAX))
print(initial_population)
current_population = initial_population
count = 1
population_fitness = [[0], [0]]
#Начало основного цикла
while (count < 20):
    population_fitness.clear()
    #fitness computing
    print("Number of population:", count)
#Оценивание популяции
    for i in range(AMOUNT_OF_POPULATION):
        population_fitness.append([fitness_function(current_population[i]), current_population[i]])
    population_fitness = sorted(population_fitness, reverse=True)
    print("fitness of best individual",population_fitness[0][1], ' = ', population_fitness[0][0])
#Селекция усечением
    sellected_population =truncation_selection(population_fitness, AMOUNT_OF_POPULATION, L)
    #Скрещивание
    k = 0
    new_population = []
    while (k < AMOUNT_OF_POPULATION):
        i = round(rand() * len(sellected_population)* L)
        j = round(rand() * len(sellected_population)* L)
        if(PC > rand()):
            BLX_a(sellected_population[i], sellected_population[j], new_population, alpha)
            k+=2
        else:
            new_population.append(sellected_population[i])
            new_population.append(sellected_population[j])
            k+=2
    #Мутация
    for i in new_population:
        if(PM > rand()):
            i = i + random.gauss(0, 1)
	#Указатель на новую популяцию
    current_population = new_population
    count += 1
