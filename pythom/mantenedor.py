import json

def menu_categoria():
 while True:
    print("******MANTENEDOR CATEGORIAS******")
    print("1. agregar categoria:")
    print("2. editar categoria:")
    print("3. eliminar categoria:")
    print("4. buscar categoria:")
    print("5. volver:")
    opcion=int(input("ingrese una opcion:"))
    
    if opcion == 1:
       print()
    elif opcion == 2:
       print()
    elif opcion ==3:
       print()
    elif opcion ==4:
       print()
    elif opcion ==5:
         
    else:
        print("opcion no valida")
    

with open ("biblioteca.json", "r", encoding="utf-8") as file:
    leerjson= json.load(file)


def agregar_categoria(nombre):
 nueva_categoria= {
        "categoriaID": (len("categoriaID"))+1,
        "nombre": nombre
    }
leerjson["categoria"].append(nueva_categoria)

def leer_categoria():
    for i in leerjson("categoria"):
        print(f""" 
             "categoria" {i}
             "nombre" {i}
              """)
        
def editar_categoria(nombre):
   categoria_ID:print(int(input("ingrese la ID:")))
for categoria in leerjson["categoria"]:
 if categoria 
   
   


 def eliminar_categoria(ID,nombre):
   categoria_ID:print (int(input("ingrese la ID de la categoria")))
for categoria in leerjson["categoria"]:
   if categoria == [categoriaID].pop:
   


 def buscar_categoria():
 categoria_ID: print (int(input("ingrese ID de la categoria:")))
 for categoria in leerjson["categoria"]:
     if categoria_ID == categoria["categoriaID"]:
         print(categoria["nombre"])



