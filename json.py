
import json

def cargar_datos(ruta):
  with open('file.json').read() as contenido:
    lineas = json.loads(contenido)
    for linea in lineas:
      print(linea)

