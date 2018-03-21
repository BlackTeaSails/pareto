import json
from solution import Solution

def load_solutions(ruta):
  importedSolutions = []
  with open(ruta) as content:
    solutions = json.load(content)
    for solution in solutions:
      importedSolutions.append(Solution(solution["satisfaction"], solution["effort"] ))

  return importedSolutions

def main():
  solutions = load_solutions("solutions.json")
  #solutions.sort()
  for solution in solutions:
    print(solution)
    # analices where the pareto front is

  # then writes the result as another json

if __name__ == '__main__':
  main()
