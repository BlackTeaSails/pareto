import json
from solution import Solution
from operator import attrgetter

def load_solutions(ruta):
  importedSolutions = []
  with open(ruta) as content:
    solutions = json.load(content)
    for solution in solutions:
      importedSolutions.append(Solution(solution["effort"], solution["satisfaction"]))

  return importedSolutions

def getParetoFront(solutions):
  paretoDict = {}
  paretoFront = []
  for solution in solutions:
    if not solution.effort in paretoDict:
      paretoDict[solution.effort] = solution.satisfaction
      continue
    if solution.satisfaction > paretoDict[solution.effort]:
      paretoDict[solution.effort] = solution.satisfaction

  for k,v in paretoDict.items():
    paretoFront.append(Solution(k, v))
  return paretoFront

def main():
  solutions = load_solutions("solutions.json")
  for s in solutions:
    print(s)
  sorted(solutions, key=attrgetter('productivity'))
  print("================Ordenadas por productividad============")
  for s in sorted(solutions, key=attrgetter('effort')):
    print(s)
  paretoFront = sorted(getParetoFront(solutions), key=attrgetter('effort'))
  print("================Frente de pareto============")
  for s in paretoFront:
    print(s)

  with open('result.json', 'w') as outfile:
    json.dump([s.__dict__ for s in paretoFront], outfile, indent=4)


  # then writes the result as another json

if __name__ == '__main__':
  main()
