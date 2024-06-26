import json

with open ("biblioteca.json", "r", encoding="utf-8") as file:
    leerjson= json.load(file) 

with open ("Reportes_biblioteca_mundo_libro.json", "w",encoding="utf-8") as file:
    json.dump(leerjson["prestamo"])