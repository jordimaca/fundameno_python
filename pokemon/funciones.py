
import requests
import re


def getprimeroultimo(lista):
    primero=None
    ultimo=None
    for pokemon in lista:
        
        idpokemon=pokemon['url'].split('/')[6]
        if primero==None:
            primero=int(idpokemon)
    ultimo=int(idpokemon)
    
    return (primero, ultimo)

def obtenerdatos(url):
    
    respuesta= requests.get(url)
    if respuesta:
        return respuesta.json()
    else:
        raise Exception("no hay datos")
    
def verlistado(url):
    print ("listado de pokemones")
    respuesta= requests.get(url)
    if respuesta:
        datos=respuesta.json()
        print(getprimeroultimo(datos['results']))
        pass
        print("{:<5}{:<15}".format('ID','nombre'))
        for pokemon in datos['results']:
            idpokemon=pokemon['url'].split('/')[6]
            nombre=pokemon['name']
            

            print("{:<5}{:<15}".format(idpokemon,nombre))

def verpokemon():
    print ("ver pokemon")
  
#-buscar un pokemon por su id
def buscarpokemonporid(num):
    #num=int(input("que pokemon desea ver?\ndigite el id de el mismo:"))
    url=f"https://pokeapi.co/api/v2/pokemon/{num}"
    datos=obtenerdatos(url)
    print (f"nombre del pokemon:{datos['name']}")
    peso=int(datos['weight'])
    peso=peso/10
    print(f"peso:{peso}kg")
    altura=int(datos['height'])
    altura=altura/10
    print(f"altura:{altura}m")
    print(f"cantidad de habilidades:{len(datos['abilities'])}")
    habilidades=[]
    tipos=[]
    for nombres in datos['abilities']:
        habilidades.append(nombres['ability']['name'])
        
        
    for i,habilidad in enumerate(habilidades,1):
        print (i,habilidad)
        
        
    print(f"cantidad de movimientos:{len(datos['moves'])}")
    
    print("tipos:")
    for nombres in datos['types']:
        tipos.append(nombres['type']['name'])
        
        
    for tipo in tipos:
        print ('*'+tipo)
        
    
def buscarpokemonpornombre():  
    name=input("que pokemon desea ver?\ndigite el nombre de el mismo:")
    url=f"https://pokeapi.co/api/v2/pokemon/{name}"
    
    datos=obtenerdatos(url)
    print (f"nombre del pokemon:{datos['name']}")
    peso=int(datos['weight'])
    peso=peso/10
    print(f"peso:{peso}kg")
    altura=int(datos['height'])
    altura=altura/10
    print(f"altura:{altura}m")
    print(f"cantidad de habilidades:{len(datos['abilities'])}")
    habilidades=[]
    tipos=[]
    for nombres in datos['abilities']:
        habilidades.append(nombres['ability']['name'])
        
        
    for i,habilidad in enumerate(habilidades,1):
        print (i,habilidad)
        
        
    print(f"cantidad de movimientos:{len(datos['moves'])}")
    
    print("tipos:")
    for nombres in datos['types']:
        tipos.append(nombres['type']['name'])
        
        
    for tipo in tipos:
        print ('*'+tipo)
    
    
def salir():
    
    print ("bye")
    
    
    

