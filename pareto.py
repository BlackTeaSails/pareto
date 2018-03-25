import json
from solution import Solution

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
  paretoFront = getParetoFront(solutions)
  for s in paretoFront:
    print(s)
  # then writes the result as another json

if __name__ == '__main__':
  main()
