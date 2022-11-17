import random
import os

def calculate_fitness(kromosom):
  fitness = 0
  tmp_pelanggaran = 0
  kesalahan = []
  for i in range(len(kromosom)):
    for j in range(len(kromosom)):
      if(i!=j  and i < j):
        bobot = 1
        pelanggaran = 0
        if (kromosom[i][0] == kromosom[j][0] and kromosom[i][3] == kromosom[j][3]):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if (kromosom[i][1] == kromosom[j][1] and kromosom[i][3] == kromosom[j][3]):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if (kromosom[i][2] == kromosom[j][2] and kromosom[i][3] == kromosom[j][3]):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if ((kromosom[i][1] == 1 and kromosom[j][1] == 3 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 3 and kromosom[j][1] == 1 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if ((kromosom[i][1] == 1 and kromosom[j][1] == 11 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 11 and kromosom[j][1] == 1 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if ((kromosom[i][1] == 11 and kromosom[j][1] == 3 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 3 and kromosom[j][1] == 11 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if ((kromosom[i][1] == 2 and kromosom[j][1] == 7 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 7 and kromosom[j][1] == 2 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        if ((kromosom[i][1] == 1 and kromosom[j][1] == 3 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 3 and kromosom[j][1] == 1 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])
        
        if ((kromosom[i][1] == 4 and kromosom[j][1] == 10 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 10 and kromosom[j][1] == 4 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])

        if ((kromosom[i][1] == 5 and kromosom[j][1] == 8 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 8 and kromosom[j][1] == 5 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])

        if ((kromosom[i][1] == 5 and kromosom[j][1] == 12 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 12 and kromosom[j][1] == 5 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])

        if ((kromosom[i][1] == 12 and kromosom[j][1] == 8 and kromosom[i][3] == kromosom[j][3]) or 
          (kromosom[i][1] == 8 and kromosom[j][1] == 12 and kromosom[i][3] == kromosom[j][3])):
          pelanggaran = pelanggaran +1
          kesalahan.append([kromosom[j], kromosom[i]])

        tmp_pelanggaran = tmp_pelanggaran + (pelanggaran*bobot)

  fitness = 1/(1+tmp_pelanggaran)

  return fitness

def create_populasi(jumlah_kromosom, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu):
  populasi = []
  for i in range(jumlah_kromosom):
    kromosom = []
    # jumlah individu dari jumlah kelas
    for i in range(jumlah_kelas*jumlah_dosen):
      individu = []

      # index 0 individu adalah kelas, 1 adalah dosen, 2 adalah ruangan, 3 adalah waktu
      individu.append(random.randint(1, jumlah_kelas))
      individu.append(random.randint(1, jumlah_dosen))
      individu.append(random.randint(1, jumlah_ruangan))
      individu.append(random.randint(1, jumlah_waktu))

      kromosom.append(individu)
    populasi.append({'kromosom':kromosom, 'fitness': calculate_fitness(kromosom)})
  return populasi

def selection(populasi):
  pro_fitness = []
  fitness_data = []
  jumlah_fitness_populasi = 0
  for i in range(len(populasi)):
    jumlah_fitness_populasi = jumlah_fitness_populasi + populasi[i]['fitness']

  for i in range(len(populasi)):
    pro_fitness.append(populasi[i]['fitness']/jumlah_fitness_populasi)
    fitness_data.append(populasi[i]['fitness'])

  index = pro_fitness.index(max(pro_fitness))
  parent1 = populasi[index]
  pro_fitness.pop(index)

  index = pro_fitness.index(max(pro_fitness))
  parent2 = populasi[index]

  return [parent1, parent2]

def crossover(parent1, parent2, crossover_rate):
  child1 = {}
  child2 = {}

  CP = round(len(parent1['kromosom']) * crossover_rate)
  child1['kromosom'] = parent2['kromosom'][0:CP]+parent1['kromosom'][CP:]
  child1['fitness'] = parent1['fitness']
  child2['kromosom'] = parent1['kromosom'][0:CP]+parent2['kromosom'][CP:]
  child2['fitness'] = parent2['fitness']

  return [child1, child2]

def mutationv2(child1, child2, mutation_rate, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu):
  jumlah_individu = len(child1)+len(child2)
  jumlah_individu_akan_termutasi = jumlah_individu*mutation_rate
  index_yang_telah_termutasi = []
  i = 0
  while(i < jumlah_individu_akan_termutasi):
    index_individu_akan_dimutasi = random.randint(0, jumlah_individu-1)
    if (index_individu_akan_dimutasi not in index_yang_telah_termutasi):
      tmp = []
      tmp.append(random.randint(1, jumlah_kelas))
      tmp.append(random.randint(1, jumlah_dosen))
      tmp.append(random.randint(1, jumlah_ruangan))
      tmp.append(random.randint(1, jumlah_waktu))
      if(index_individu_akan_dimutasi  < len(child1)):
        child1[index_individu_akan_dimutasi] = tmp
      else:
        child2[index_individu_akan_dimutasi-(len(child1)-1)] = tmp
      index_yang_telah_termutasi.append(index_individu_akan_dimutasi)
      i = i + 1
  return [child1, child2]
  

def mutation(child1, mutation_rate, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu):
  
  tmp = child1['kromosom'].copy()

  for i in range(len(tmp)):
    if (random.random() <= mutation_rate):
      tmp[i] = []
      tmp[i].append(random.randint(1, jumlah_kelas))
      tmp[i].append(random.randint(1, jumlah_dosen))
      tmp[i].append(random.randint(1, jumlah_ruangan))
      tmp[i].append(random.randint(1, jumlah_waktu))
  
  return {
    'kromosom': tmp,
    'fitness': child1['fitness']
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

  if (the_best_solution['fitness'] == 1.0):
    return [False, the_best_solution]
  else:
    return [True, the_best_solution]

def logging(populasi, solusi, generasi):

  print("Solusi :", solusi['kromosom'])
  print("Generasi :", generasi)
  
  for i in range(len(populasi)):
    print('| Fitness :', populasi[i]['fitness'])

jumlah_kelas = 3
jumlah_dosen = 13
jumlah_ruangan = 9
jumlah_waktu = 20

jumlah_kromosom = 5
generasi = 0
mutation_rate = 0.2
crossover_rate = 0.5

populasi = create_populasi(jumlah_kromosom, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu)

generasi = 0
isLooping = True

while(isLooping):
  [parent1, parent2] = selection(populasi)

  [child1, child2] = crossover(parent1, parent2, crossover_rate)

  mutant1 = mutation(child1, mutation_rate, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu)
  mutant2 = mutation(child2, mutation_rate, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu)
  # [mutant1, mutant2] = mutationv2(child1, child2, mutation_rate, jumlah_dosen, jumlah_kelas, jumlah_ruangan, jumlah_waktu)

  mutant1['fitness'] = calculate_fitness(mutant1['kromosom'])
  mutant2['fitness'] = calculate_fitness(mutant2['kromosom'])

  children = [mutant1, mutant2]

  populasi = regeneration(populasi, children)
  generasi = generasi + 1

  [isLooping, solusi] = termination(populasi)

  os.system('cls||clear')
  logging(populasi, solusi, generasi)





