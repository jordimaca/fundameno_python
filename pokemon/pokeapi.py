"""
-hacer un programa que muestre un listado con los pokemones,
el usuario tendra la oportunidad de digitar su id correspondiente,
y se le mostrara la informacion relacionada al mismo.
-ademas el usuario podra navegar en el programa mediante shorcuts y/o teclas del teclado
-algunas opciones seran:
-ver siguiente/anterior listado
-ver siguiente/anterior pokemon
-salir del programa
-buscar un pokemon por su id
-buscar un pokemon por su nombre
"""

import requests
import keyboard



#idpokemon=pokemon['url'].split('/')[6]
def pkmon():
    num=int(input("que pokemon desea ver?\ndigite el numero de el mismo:"))
    url=f"https://pokeapi.co/api/v2/pokemon/{num}"
    respuesta=requests.get(url)
    #print("status code: ", respuesta.status_code)
    datos=respuesta.json()
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
        
        
    for i,tipos in enumerate(tipos,1):
        print (i,tipos)
        
        
    while True:
        print("Si desea  ver el siguiente  pokemon presione (s)\nSi desea ver el anterior pokemon presione (a)\nSi desea terminar presione (x)")
     
        if keyboard.read_key()=='s':
            num=num+1
            url=f"https://pokeapi.co/api/v2/pokemon/{num}"
            respuesta=requests.get(url)
            #print("status code: ", respuesta.status_code)
            datos=respuesta.json()
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
        
        
            for i,tipos in enumerate(tipos,1):
                print (i,tipos)

 
        elif keyboard.read_key()=='a':
            num=num-1
            url=f"https://pokeapi.co/api/v2/pokemon/{num}"
            respuesta=requests.get(url)
            #print("status code: ", respuesta.status_code)
            datos=respuesta.json()
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
        
        
            for i,tipos in enumerate(tipos,1):
                print (i,tipos)


        
     
                
        elif keyboard.read_key()=='x':
            break   
    
        

    
        
def listapk():
 
    limit=int(input("cuantos pokemons desea ver por pagina?:"))
    
    
    offset=0
    
        
    url=f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
        
      
    
    respuesta=requests.get(url)
    if respuesta:
        datos=respuesta.json()
    pokemon=[]
    for nombres in datos['results']:
        pokemon.append(nombres['name'])
        
    for i,pk in enumerate(pokemon,offset):
        print(i+1,pk)
        
    while True:
        print(f"Si desea  ver los siguientes {limit} pokemons presione (s)\nSi desea ver los anteriores {limit} pokemons presione (a)\nSi desea terminar presione (x)")
     
        if keyboard.read_key()=='s':
            url=datos['next']
        
            respuesta=requests.get(url)
            if respuesta:
                datos=respuesta.json()
            pokemon=[]
            for nombres in datos['results']:
                pokemon.append(nombres['name'])
                
            offset= offset+limit
        
            for pk in pokemon:
                print(pk)
                
            offset= offset+limit 
        elif keyboard.read_key()=='a':
            url=datos['previous']
        
            respuesta=requests.get(url)
            if respuesta:
                datos=respuesta.json()
            pokemon=[]
            for nombres in datos['results']:
                pokemon.append(nombres['name'])
                
            offset=offset-limit        
            for pk in pokemon:
                print(pk) 
            
                
        elif keyboard.read_key()=='x':
            break   
    
                 
   
        
    

        
    
"""        
keyboard.add_hotkey('ctrl+a', print, args=('anterior...', 'hotkey'))
keyboard.add_hotkey('ctrl+w', print, args=('siguiente...', 'hotkey'))
keyboard.wait('esc')
"""


print("Bienvenido a la pokedex:\n")  


pkmon()

    