import random
import os


# representasi dari gen
def create_gen(panjang_gen):
  i = 0
  listChar = []
  while(i < panjang_gen):
    random_int = random.randint(32, 126)
    listChar.append(chr(random_int))
    i = i + 1
  random_gen = "".join(listChar)
  return random_gen

# fitness funtion
def calculate_fitness(gen, target):
  jumlah_benar = 0
  panjang_target = len(target)
  i = 0
  while(i < panjang_target):
    if (gen[i] == target[i]):
      jumlah_benar = jumlah_benar + 1
    i=i+1
  fitness = (jumlah_benar/panjang_target)*100
  return fitness
  
def create_populasi(target, besar_populasi):
  populasi = []
  for i in range(besar_populasi):
    gen = create_gen(len(target))
    populasi.append({
      'gen': gen,
      'fitness' : calculate_fitness(gen, target)
    })
  return populasi

def selection(populasi):
  fitness_data = []
  for i in range(len(populasi)):
    fitness_data.append(populasi[i]['fitness'])

  index = fitness_data.index(max(fitness_data))
  parent1 = populasi[index]

  fitness_data.pop(index)

  index = fitness_data.index(max(fitness_data))
  parent2 = populasi[index]

  return [parent1, parent2]


def crossover(parent1, parent2):
  child1 = {}
  child2 = {}
  CP = round(len(parent1['gen'])/2)
  child1['gen'] = parent2['gen'][0:CP]+parent1['gen'][CP:]
  child1['fitness'] = parent1['fitness']
  child2['gen'] = parent1['gen'][0:CP]+parent2['gen'][CP:]
  child2['fitness'] = parent2['fitness']

  return [child1, child2]

def mutation(child, laju_mutasi):

  tmp =  list(child['gen'])

  for i in range(len(child['gen'])):
    if ( random.random() <= laju_mutasi ):
      tmp[i] = chr(random.randint(32, 126)) 

  return {
    'gen': ''.join(tmp),
    'fitness': child['fitness']
  }

def regeneration(populasi, children):

  fitness = []

  new_populasi = populasi.copy()

  for i in range(len(new_populasi)):
    fitness.append(new_populasi[i]['fitness'])

  for i in range(len(children)):
    index = fitness.index(min(fitness))
    new_populasi.pop(index)
    fitness.pop(index)
  
  for i in range(len(children)):
    new_populasi.append(children[i])

  return new_populasi

def termination (populasi):
  the_best_solution = selection(populasi)[0]

  if (the_best_solution['fitness'] == 100):
    return [False, the_best_solution]
  else:
    return [True, the_best_solution]

def logging(populasi,target, solusi, generasi):
  print("Target :", target)
  print("Solusi :", solusi['gen'])
  print("Generasi :", generasi)
  
  for i in range(len(populasi)):
    print("Gen :", populasi[i]['gen'], '| Fitness :', populasi[i]['fitness'])


target = 'WiroSableng'
besar_populasi = 10
laju_mutasi = 0.2
populasi = create_populasi(target, besar_populasi)

generasi = 0
isLooping = True
while(isLooping):
  [parent1, parent2] =  selection(populasi)

  # coress over
  [child1, child2] = crossover(parent1, parent2)
  # Mutasi
  mutant1 = mutation(child1, laju_mutasi)
  mutant2 = mutation(child2, laju_mutasi)

  # # hitung fitness mutant
  mutant1['fitness'] = calculate_fitness(mutant1['gen'], target)
  mutant2['fitness'] = calculate_fitness(mutant2['gen'], target)


  children = [mutant1, mutant2]
  populasi = regeneration(populasi, children)
  generasi = generasi + 1

  [isLooping, solusi] = termination(populasi)
  os.system('cls||clear')
  logging(populasi, target, solusi, generasi)





