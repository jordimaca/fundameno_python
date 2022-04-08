
import requests
import re
from funciones import *
#from tabulate import tabulate

print("mostrando primeros 20 pokemons:")

baseurl = "https://pokeapi.co/api/v2/"
url = baseurl+"pokemon?limit=20&offset=0"
regexnum = "^[0-9]{1,3}$"
verlistado(url)
listadopokemones = obtenerdatos(url)
primeroultimo = getprimeroultimo(listadopokemones['results'])

primero = primeroultimo[0]
ultimo = primeroultimo[1]

cont=0
while cont==0:
    pregunta=input("desea buscar el pokemon por id(i) o por nombre(n)")
    if pregunta=='i':
        
        iddigit = input(f"digite un id[{primero}-{ultimo}]: ")


        while (not re.search(regexnum, iddigit)) or (int(iddigit) < primero or int(iddigit) > ultimo):
            iddigit = input(f"digite un id [{primero}-{ultimo}]: ")
        buscarpokemonporid(iddigit)
        cont=1
    elif pregunta=='n':
        buscarpokemonpornombre()
        cont=1
        
    else:
        print ("digite correctamente")
        

    
        





#titulo=['id','nombre','peso','altura', 'habilidades','movimientos']
#print(tabulate(titulo, headers='firstrow', tablefmt='fancy_grid'))
