from cola import Cola
# Entre una función y otra solo cambia la condición que se comprueba
# Busca a Capitana Marvel y muestra su nombre real.
def buscar_personaje_de_capitana_marvel(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        personaje = cola.atencion()

        if personaje["superheroe"] == "Capitana Marvel":
            print("El personaje de Capitana Marvel es:", personaje["nombre"])
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

# Muestra los nombres de superhéroes cuyo género es F.
def mostrar_superheroes_femeninos(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        personaje = cola.atencion()

        if personaje["genero"] == "F":
            print(personaje["superheroe"])
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

# Muestra los nombres reales de personajes cuyo género es M.
def mostrar_personajes_masculinos(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        personaje = cola.atencion()

        if personaje["genero"] == "M":
            print(personaje["nombre"])
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

# Busca a Scott Lang y muestra su nombre de superhéroe.
def buscar_superheroe_de_scott_lang(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        personaje = cola.atencion()

        if personaje["nombre"] == "Scott Lang":
            print("El superhéroe de Scott Lang es:", personaje["superheroe"])
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

# Muestra los personajes cuyo nombre real o nombre de superhéroe comienza con S.
def mostrar_datos_con_s(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        personaje = cola.atencion()

        if (
            personaje["nombre"].startswith("S")
            or personaje["superheroe"].startswith("S")
        ):
            print(personaje)
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

# Comprueba si Carol Danvers está en la cola y muestra su nombre de superhéroe.
def buscar_carol_danvers(cola):
    cantidad = cola.tamanio()
    encontrado = False # encontrado = False: inicialmente suponemos que Carol no está.

    for _ in range(cantidad):
        personaje = cola.atencion()

        if personaje["nombre"] == "Carol Danvers":
            print("Carol Danvers se encuentra en la cola.")
            print("Su nombre de superhéroe es:", personaje["superheroe"])
            encontrado = True # encontrado = True: cambiamos el valor cuando la encontramos.
 # Acá se comprueba la condición de búsqueda
        cola.arribo(personaje)

    if not encontrado: # if not encontrado: si la bandera sigue siendo False al terminar, informamos que no está.
        print("Carol Danvers no se encuentra en la cola.")


# Programa principal

cola_mcu = Cola()

cola_mcu.arribo({
    "nombre": "Tony Stark",
    "superheroe": "Iron Man",
    "genero": "M"
})

cola_mcu.arribo({
    "nombre": "Steve Rogers",
    "superheroe": "Capitán América",
    "genero": "M"
})

cola_mcu.arribo({
    "nombre": "Natasha Romanoff",
    "superheroe": "Black Widow",
    "genero": "F"
})

cola_mcu.arribo({
    "nombre": "Carol Danvers",
    "superheroe": "Capitana Marvel",
    "genero": "F"
})

cola_mcu.arribo({
    "nombre": "Scott Lang",
    "superheroe": "Ant-Man",
    "genero": "M"
})

cola_mcu.arribo({
    "nombre": "Stephen Strange",
    "superheroe": "Doctor Strange",
    "genero": "M"
})

cola_mcu.arribo({
    "nombre": "Shuri",
    "superheroe": "Black Panther",
    "genero": "F"
})

cola_mcu.arribo({
    "nombre": "Sam Wilson",
    "superheroe": "Falcon",
    "genero": "M"
})


print("COLA ORIGINAL:")
cola_mcu.mostrar()

print("\nA) PERSONAJE DE CAPITANA MARVEL:")
buscar_personaje_de_capitana_marvel(cola_mcu)

print("\nB) SUPERHÉROES FEMENINOS:")
mostrar_superheroes_femeninos(cola_mcu)

print("\nC) PERSONAJES MASCULINOS:")
mostrar_personajes_masculinos(cola_mcu)

print("\nD) SUPERHÉROE DE SCOTT LANG:")
buscar_superheroe_de_scott_lang(cola_mcu)

print("\nE) DATOS CUYO NOMBRE O SUPERHÉROE COMIENZA CON S:")
mostrar_datos_con_s(cola_mcu)

print("\nF) BUSCAR CAROL DANVERS:")
buscar_carol_danvers(cola_mcu)
