
import json

leer = json.loads(open('file.json').read())

print leer[0]['isActive']

