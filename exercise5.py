import random

def dups (a, b): 
  max_num = max(a,b)
  min_num = min(a,b)
  print(max_num)
  print(min_num)

  final = []

  for elem in max_num:
    if (elem in min_num and elem not in final):
      final.append(elem)

  return final

def rand_list_gen(lis_len):
  i = 0
  lis = []
  while i < lis_len:
    num = random.randrange(1, 100)
    lis.append(num)
    i += 1
  return lis

duplicates = dups(rand_list_gen(11), rand_list_gen(15))
print('Duplicates: ', duplicates)  

showed_interest = [
'Jasmine Humbert', 'Asim Zaidi', 'Jaeson Booker', 'Marianna Campbell', 'Zurich Okoren','Erik Batista', 'Lucia Reynoso', 'Anwar Azeez', 'Jamar Gibbs', 'Anisha Jain', 'Sarin Swift', 'Rinni Swift', 'Fodé Diop', 'Jackson Ho', 'Nathan Pillai', 'Dacio Romero', 'William Bogans', 'Salvador Becerra', 'Jamie McCrory'
]

vantaggio_residents = [ 
  'Anisha Jain', 'Colleen Ni', 'Dacio Romero', 'Edwin Cloud', ''

]

Edwin Cloud, Dylan Finn, Ramon Geronimo Adames, Samuel Harrison, Matthew Phraxayavong, Jonathan Kopp, Ricardo Rodriguez Orrego, Jeremy James, Kymm Wilson, Matthew Harrilal

Severiano Badajoz, Anne Bailey, Ebonne Cabarrus, Connor Cahill, Stephanie Cherubin, Sean Glancy, Drake Vorndran, Noah Woodward, Erica Naglik, Cherish Kim = 11