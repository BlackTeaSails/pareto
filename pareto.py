import json
from solution import Solution

def load_solutions(ruta):
  importedSolutions = []
  with open(ruta) as content:
    solutions = json.load(content)
    for solution in solutions:
      importedSolutions.append(Solution(solution["satisfaction"], solution["effort"] ))

  return importedSolutions

def compararSoluciones(solutions):
    solucionesPareto = []
    for solution in solutions:
        print(solution)
        aux = solution
        for solution2 in solutions:
            # Buscamos las soluciones con el mismo esfuerzo
            if ((int)solution2.effort == (int)aux.effort) :
                # Si la nueva solucion tiene mas satisfaccion la añadimos a la comparacion
                if ((int)solution2.satisfaction > (int)aux.satisfaction)) :
                    aux = solution2.effort
        # La solucion con mayor satisfaccion para un esfuerzo, se añade
        solucionesPareto.append(aux)
    return solucionesPareto

def main():
  solutions = load_solutions("solutions.json")
  solucionesPareto = []
  for solution in solutions:
    print(solution)

  #para ordenar por "productivity"
  #solutions.sort()

  # analices where the pareto front is
  solucionesPareto = compararSoluciones(solutions)

  # then writes the result as another json

if __name__ == '__main__':
  main()
