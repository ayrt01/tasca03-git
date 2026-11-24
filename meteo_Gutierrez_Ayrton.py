import random

#1.1 Dades de partida
#Copieu aquestes dades al principi del programa. Els dies de la setmana són una tupla perquè no han de canviar mai.

#Tupla con los 7 dias de la semana
dies = ("Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge")

#Lista de nombres de las ciudades
ciutats_catalanes = [
    "Barcelona", "Girona", "Lleida", "Tarragona", "Badalona",
    "Sabadell", "Terrassa", "Mataró", "Reus", "Vic",
    "Manresa", "Granollers", "Figueres", "Olot", "Blanes",
    "Cerdanyola del Vallès", "Esplugues de Llobregat", "Gavà",
    "Sant Feliu de Llobregat", "Vilafranca del Penedès",
    "El Prat de Llobregat", "Vilanova i la Geltrú", "Cambrils",
    "Castelldefels", "L'Hospitalet de Llobregat"
  ]
 
#Lista de las precipitaciones posibles
precipitacions_possibles = [0, 0, 5, 10, 15, 20, 0, 0, 0, 0, 5, 0,
                            0, 0, 10, 0, 0, 0, 0, 0, 5, 0, 0, 0]

#1.2 Generació de les dades
#Genereu una llista anomenada dades_meteorologiques amb un diccionari per a cada ciutat. Cada diccionari tindrà aquesta estructura:
#Cada llista té 7 valors, un per a cada dia de la setmana, en el mateix ordre que la tupla dies.
#Temperatures: enters entre 5 i 25, tots dos inclosos (random.randint).
#Precipitacions: valors escollits a l'atzar de la llista precipitacions_possibles (random.choice).
#Humitat: enters entre 40 i 80, tots dos inclosos.
#És obligatori generar les dades amb list comprehensions.

#List comprehension, por cada ciudad crea un diccionario
dades_meteorologiques = [{
                        #El nombre de la ciudad actual del bucle
                        "Ciutat": nom_ciutat, 
                        #Lista de 7 temperaturas enteras entre 5 y 25, una por dia, el _ es una variable que no se usa
                        "Temperatures": [random.randint(5,25) for _ in range(len(dies))],
                        #Lista de 7 valores de precipitaciones elegidos al azar de la lista de precipitaciones posibles con random choice
                        "Precipitacions": [random.choice(precipitacions_possibles) for _ in range(len(dies))],
                        #Lista de 7 valores de humedad entre 40 y 80
                        "Humitat":[random.randint(40,80) for _ in range(len(dies))]
                        }
                        #Repite todo el diccionario por cada ciudad de la lista ciudades catalanas
                        for nom_ciutat in ciutats_catalanes]

#Imprime la cabecera de la tabla
print(f'{"Ciutat":<30}{"Temperatures":<30}{"Precipitacions":<30}{"Humitat":<30}')
print("-" * 120)
print()

#Recorre los 25 diccionarios para imprimir una fila con sus datos
for d in dades_meteorologiques:
    #Saca el nombre de la ciudad del diccionario
    ciutat = d["Ciutat"]
    #Convierte la lista de temperaturas en un str(texto) para poder alinearla con :<30
    temps = str(d["Temperatures"])
    #Repetimos lo mismo que con la anterior
    precip = str(d["Precipitacions"])
    #Volvemos a repetirlo una ultima vez
    hum = str(d["Humitat"])
    
    #Imprime la fila, cada columna de dato cuenta con 30 caracteres
    print(f"{ciutat:<30}{temps:<30}{precip:<30}{hum:<30}")

print()
#Part 2: Aplicació
#Feu un menú amb les opcions següents. El menú s'ha de tornar a mostrar després de cada opció, fins que l'usuari triï 0. Si l'usuari escriu un valor que no és un número entre 0 i 10, s'ha de mostrar un missatge d'error i tornar a demanar l'opció.

#Flag que controla el bucle, empieza en false
sortida= False

#Bucle principal, mostrara el menu una y otra vez mientras sortida sea False
while not sortida:
    #Titulo del menu
    print("Aplicació meteo-DAW")
    print("=" * 120)
    #Opciones del menu
    print("0  Sortir")
    print("1  Mitjana de temperatures per ciutat")
    print("2  Ciutats amb precipitació màxima")
    print("3  Dia de la setmana més calorós")
    print("4  Ordenació de ciutats per temperatura mitjana (ascendent)")
    print("5  Cerca dicotòmica de ciutat per nom")
    print("6  Freqüència de temperatures i gràfic")
    print("7  Consultes de precipitacions amb conjunts")
    print("8  Màxim, mínim i mitjana d'humitat")
    print("9  Ciutats amb temperatures superiors a un llindar")
    print("10 Comparar temperatures entre dues ciutats")

    #Pide al usuario escojer una opcion, lo que se introduzca llegara en formato de texto
    opcion= input("Escull una de les opcions: ").strip()
    
    #Comprueba que el texto introducido sea un numero
    if opcion.isdigit():
        #Lo convierte en un numero entero
        opcion= int(opcion)
        #Comprueba que el numero este entre 0 y 10 (Ambos incluidos)
        if 0 <= opcion <= 10:
            print()
            
            #Opció 0. Sortida
            if opcion == 0:
                #Salida del programa
                sortida= True

            #Opció 1. Mitjana de temperatures per ciutat
            elif opcion == 1:
                #Imprime el titulo 
                print("Mitjana de temperatures per ciutat")
                print("=" * 120)
                #Recorre cada diccionario de la lista de diccionarios
                for d in dades_meteorologiques:
                    #Media= suma de todos los datos de la lista temperaturas, dividida entre cuantas hay
                    mitjana= sum(d['Temperatures']) / (len(d['Temperatures']))
                    #Imprime la ciudad y la media con dos decimales
                    print(f"{d['Ciutat']}: {mitjana: .2f} ºC" )
                print()
                
            #Opció 2. Ciutats amb precipitació màxima
            elif opcion == 2:
                #Imprime el titulo
                print("Ciutats amb precipitació màxima")
                print("=" * 120)
                #Diccionario vacio donde se guardara la ciudad y la lluvia total de la semana
                max_precipitació= {}
                #Recorre cada ciudad
                for ciutat in dades_meteorologiques:
                    #Sumamos la precipitacion de los 7 dias
                    precipitació_total= sum(ciutat['Precipitacions'])
                    #Mostramos la ciudad, con la lista de precipitaciones, y su total
                    print(f"{ciutat['Ciutat']}: {ciutat['Precipitacions']} - TOTAL = {precipitació_total} mm")
                    #Añadimos al diccionario, usando el nombre de la ciudad como clave, y la precipitacion total como valor
                    max_precipitació[ciutat["Ciutat"]]= precipitació_total
                #Buscamos dentro de los valores del diccionario que serian las precipitaciones totales, la mas alta
                p_max_ciudad= max(max_precipitació.values())
                #Creamos una lista con las ciudades que tengan el mismo valor maximo, asi guardamos aparte las ciudades que compartan la precipitacion mas alta
                ciudades_p_max= [k for k, v in max_precipitació.items() if v == p_max_ciudad]
                print()
                #Imprimimos la precipitacion mas alta de la semana
                print(f"Precipitació màxima de la setmana: {p_max_ciudad} mm")
                #Imprimimos las ciudades con las precipitaciones mas altas
                print(f"Ciutat/s: {', '.join(ciudades_p_max)}")
                print()
            
            #Opció 3. Dia de la setmana més calorós 
            elif opcion == 3:
                #Imprime el titulo
                print("Dia de la setmana més calorós")
                print("=" * 120)
                #Creamos un diccionario que guarda el dia como clave y la temperatura media de ese dia entre todas las ciudades
                mes_calor = {}
                #Recorremos los 7 dias por posicion
                for i in range(len(dies)):
                    #Acumulador que suma las temperaturas de ese dia
                    suma_temps = 0
                    #Recorremos todas las ciudades
                    for c in dades_meteorologiques:
                        #Sumamos la temperatura de esa ciudad en el dia i (0, 1, 2, ...)
                        suma_temps += c["Temperatures"][i]
                    #Media del dia
                    mitjana_dia = suma_temps / len(dades_meteorologiques)
                    #Imprimimos el dia y la media con 2 decimales
                    print(f"{dies[i]}: {mitjana_dia:.2f} ºC")
                    #Guardamos la media en el diccionario con el nombre de dia como llave y la media como valor
                    mes_calor[dies[i]] = mitjana_dia
                
                print()
                #Devuelve el dia con el valor mas alto
                dia_max = max(mes_calor, key=mes_calor.get)
         
                #Imprime el dia mas caluroso con su media
                print(f"El dia més calorós ha estat: {dia_max} ({mes_calor[dia_max]:.2f} ºC de mitjana)")
                print()
                
            #Opció 4. Ordenació de ciutats per temperatura mitjana
            elif opcion == 4:
                #Imprime el titulo
                print("Ordenació de ciutats per temperatura mitjana")
                print("=" * 120)
                print("Sense ordenar: ")
                print("-" * 120)
                
                #Lista de tuplas (ciudad, media)
                l=[((conjunts['Ciutat']), sum(conjunts['Temperatures']) / (len(conjunts['Temperatures']))) for conjunts in dades_meteorologiques]
                
                #Recorremos la lista sin ordenar, separando cada tupla en ciudad y media
                for ciutat, mitjana in l:
                    #Imprimimos cada ciudad con su media
                    print(f"{ciutat}: {mitjana: .2f} ºC")
                    
                #Imprimimos el titulo de la lista ordenada
                print("Ordenades (ascendent): ")
                print("-" * 120)
                
                #Ordenacion por insercion, empieza en el segundo elemento
                for i in range(1, len(l)):
                    #Guarda el elemento que hay que colocar en la posicion i
                    actual = l[i]
                    #Valor que hara referencia al elemento aterior
                    j = i - 1
                    #Mientras queden elementos a la izquierda y mientras que la media anterior sea mayor a la actual
                    while j >= 0 and l[j][1] > actual[1]:
                        #Desplaza el elemento a la derecha
                        l[j + 1] = l[j]
                        #Retrocedemos al elemento de la izquierda
                        j -= 1
                    #Colocamos el elemento actual en la posicion anterior
                    l[j + 1] = actual
            
                #Recorremos la lista ya ordenada
                for ciutat, mitjana in l:
                    #Imprimimos cada ciudad con su media
                    print(f"{ciutat}: {mitjana: .2f}")
                print()
                
            #Opció 5. Cerca dicotòmica de ciutat per nom
            elif opcion == 5:
                #Imprimimos el titulo
                print("Cerca dicotòmica de ciutat per nom")
                print("=" * 120)
                
                #Lista de nombres en minuscula y ordenada (la busqueda binaria solo funciona en listas ordenadas)
                l = sorted([conjunts['Ciutat'].lower() for conjunts in dades_meteorologiques])
                
                #Pedimos una ciudad
                valor = input("Introdueix una ciutat (o 'sortir' per tornar al menú): ").strip().lower()
                #Repetimos hasta que el usuario escriba sortir
                while valor != 'sortir':
                    #Si lo escritos son solo numeros imprime un aviso
                    if valor.isdigit():
                        print("Error: has d'introduir un nom de ciutat, no un número.")
                    #Si no, hace la busqueda binaria
                    else:  
                        #Inferior
                        inf = 0
                        #Superior
                        sup = len(l) - 1
                        #Flag = False, no se ha encontrado
                        trobat = False
                        
                        #Mientras quede zona por mirar y no se haya encontrado:
                        while inf <= sup and not trobat:
                            #Calculamos el elemento de la mitad
                            mig = (inf + sup) // 2
                            #Si el elemento central es igual al elemento que buscamos:
                            if l[mig] == valor:
                                #Marca encontrado y salimos del bucle
                                trobat = True
                            #Si la ciudad va antes que la central
                            elif valor < l[mig]:
                                #Descartamos la mitad derecha, y miramos a la izquierda
                                sup = mig - 1
                            #Si va despues
                            else:
                                #Descartamos la mitad izquierda, y miramos a la derecha
                                inf = mig + 1
                        #Cuando termine la busqueda, si se ha encontrado imprimira:
                        if trobat:
                            #Posicion donde se encontro
                            print(f"Trobat a la posició {mig + 1}")
                        #Y si no se encontro:
                        else:
                            #No encontado
                            print("No trobat")
                    print()
                    #Pide otra ciudad o sortir
                    valor = input("Introdueix una altra ciutat (o 'sortir' per tornar): ").strip().lower()
                print()
                
            #Opció 6. Freqüència de temperatures i gràfic
            elif opcion == 6:
                #Lista de tuplas con (Temperatura, las veces que aparece)
                vegades = []
                #Recorremos todas las temperaturas posibles desde 5 a 25
                for i in range(5, 26):
                    #Acumulador que suma las veces que aparece la temperatura i
                    suma_freq = 0
                    #Recorremos cada diccionario de la lista de diccionarios
                    for d in dades_meteorologiques:
                        #Recorremos la lista de temperaturas de cada ciudad
                        for t in d["Temperatures"]:
                            #Si la temperatura es igual a la que estamos contando, sumamos 1 al acumulador
                            if t == i:
                                suma_freq += 1
                    #Añadimos a la lista de tuplas la temperatura y las veces que aparece
                    vegades.append((i, suma_freq))
                    #Imprimimos la temperatura y las veces que aparece
                    print(f"Temperatura {i} ºC apareix {suma_freq} vegades")
                
                #Gráfico de temperaturas
                max_vegades = 0
                #Recorremos la lista de tuplas para encontrar el valor máximo de veces que aparece una temperatura
                for k, v in vegades:
                    #Si el valor de veces que aparece es mayor que el máximo actual, lo actualizamos
                    if v > max_vegades:
                        max_vegades = v
                        
                #Creamos una lista para guardar las temperaturas que aparecen el máximo de veces
                max_frequents = []
                #Recorremos la lista de tuplas para encontrar las temperaturas que aparecen el máximo de veces
                for k, v in vegades:
                    #Si el valor de veces que aparece es igual al máximo, añadimos la temperatura a la lista
                    if v == max_vegades:                        
                        max_frequents.append(k)
                        
                print()
                #Imprimimos las temperaturas que aparecen el máximo de veces y cuantas veces aparecen
                print(f"Temperatura més freqüent: {', '.join(str(t) for t in max_frequents)} ºC ({max_vegades} vegades)")
                print()
                #Imprimimos el gráfico de temperaturas
                print("Gràfic de temperatures")
                print("=" * 120)
                
                #Imprimimos cada temperatura y un asterisco por cada vez que aparece
                for d in vegades:
                    print(f"{d[0]:2d} |" + " * " * d[1])
                
                #Imprimimos la linea horizontal del gráfico
                print(" " * 3 + "+" + "-" * (max_vegades * 3))
                #Espacio que va antes de los numeros del eje x del gráfico
                print(" " * 4, end="")
                #Imprimimos los numeros del eje x del gráfico, con un espacio entre cada número
                for i in range(1, max_vegades + 1):
                    if i < 10:
                        print(f" {i} ", end="")
                    else: 
                        print(i, end=" ")
                print()
                
            #Opció 7. Consultes de precipitacions amb conjunts
            elif opcion == 7:
                #Creamos un diccionario donde la clave es el dia y el valor es un conjunto de ciudades donde ha llovido ese dia
                pluja_per_dia = {}
                #Recorremos cada dia de la semana
                for d in dies:
                    #Creamos un conjunto vacio para cada dia
                    pluja_per_dia[d] = set()
                    #Recorremos cada ciudad de la lista de diccionarios
                    for c in dades_meteorologiques:
                        #Buscamos la posicion del dia en la tupla de dias
                        posició = dies.index(d)
                        #Si la precipitacion de ese dia es mayor que 0, añadimos la ciudad al conjunto del dia
                        if c["Precipitacions"][posició] > 0:
                            pluja_per_dia[d].add(c["Ciutat"])
                #Imprimimos el diccionario de dias con las ciudades donde ha llovido
                for dia, ciutat in pluja_per_dia.items():
                    print(f"{dia}: {ciutat}")
                print()
                
                #Creamos un diccionario donde la clave es la ciudad y el valor es un conjunto de dias donde ha llovido esa ciudad
                pluja_per_ciutat = {}
                #Recorremos cada ciudad de la lista de diccionarios
                for ciutat in dades_meteorologiques:
                    #Guardamos el nombre de la ciudad en minuscula para usarlo como clave
                    nom_ciutat = ciutat["Ciutat"].lower()
                    #Creamos un conjunto vacio para cada ciudad
                    pluja_per_ciutat[nom_ciutat] = set()
                
                    #Recorremos cada dia de la semana para ver si ha llovido en esa ciudad
                    for i in range(len(dies)):
                        #Si la precipitacion de ese dia es mayor que 0, añadimos el dia al conjunto de la ciudad
                        if ciutat["Precipitacions"][i] > 0:
                            pluja_per_ciutat[nom_ciutat].add(dies[i])
                #Imprimimos el diccionario de ciudades con los dias donde ha llovido
                for ciutat, dia in pluja_per_ciutat.items():
                    print(f"{ciutat}: {dia}")
                print()
                
                #Pedimos al usuario que introduzca dos ciudades para comparar los dias de lluvia
                print("Comparació de precipitacions entre dues ciutats")
                print("=" * 120)
                #Pedimos la primera ciudad y la convertimos a minuscula y quitamos espacios al principio y al final        
                ciutat1 = input("Introdueix la primera ciutat: ").strip().lower()
                #Mientras la ciudad no esté en el diccionario de ciudades con lluvia, pedimos otra ciudad
                while ciutat1 not in pluja_per_ciutat:
                    #Si la ciudad no está en el diccionario, imprimimos un mensaje de error
                    print("La ciutat no es troba a la llista.")
                    #Volvemos a pedir la ciudad
                    ciutat1 = input("Introdueix la primera ciutat: ").strip().lower()
                
                #Pedimos la segunda ciudad y la convertimos a minuscula y quitamos espacios al principio y al final
                ciutat2 = input("Introdueix la segona ciutat: ").strip().lower()
                #Mientras la ciudad no esté en el diccionario de ciudades con lluvia o sea la misma que la primera ciudad, pedimos otra ciudad
                while ciutat2 not in pluja_per_ciutat or ciutat1 == ciutat2:
                    #Si la ciudad no está en el diccionario, imprimimos un mensaje de error
                    if ciutat2 not in pluja_per_ciutat:
                        print("La ciutat no es troba a la llista.")
                    #Si la ciudad es la misma que la primera, imprimimos un mensaje de error
                    else:
                        print("Has d'escollir una altra ciutat diferent.")
                    #Volvemos a pedir la ciudad
                    ciutat2 = input("Introdueix la segona ciutat: ").strip().lower()
                    
                #Obtenemos los conjuntos de dias de lluvia para cada ciudad
                dies1 = pluja_per_ciutat[ciutat1]
                dies2 = pluja_per_ciutat[ciutat2]
                
                #Imprimimos los resultados de la comparación de dias de lluvia entre las dos ciudades
                print(f"A {ciutat1} ha plogut: {dies1}")
                print(f"A {ciutat2} ha plogut: {dies2}")
                #Imprimimos los dias que han llovido en ambas ciudades, en la primera pero no en la segunda, en una de las dos, y en alguna de las dos
                print("Dies que ha plogut a les dues ciutats:", dies1 & dies2)
                print("Dies que ha plogut a la primera pero no a la segona:", dies1 - dies2)
                print("Dies que ha plogut nomes en una de les dues:", dies1 ^ dies2)
                print("Dies que ha plogut en alguna de les dues:", dies1 | dies2)
                print()
                
                #Pedimos al usuario que introduzca dos dias de la semana para comparar las ciudades donde ha llovido
                print("Comparació de precipitacions entre dos dies de la setmana")
                print("=" * 120)
                #Pedimos el primer dia y lo convertimos a minuscula y quitamos espacios al principio y al final
                dia1 = input("Introdueix un dia de la setmana: ").strip().capitalize()
                #Mientras el dia no esté en el diccionario de dias con lluvia, pedimos otro dia
                while dia1 not in pluja_per_dia:
                    print("El dia introduït no es troba a la llista")
                    dia1 = input("Introdueix un dia de la setmana: ").strip().capitalize()
                #Pedimos el segundo dia y lo convertimos a minuscula y quitamos espacios al principio y al final
                dia2 = input("Introdueix un dia de la setmana: ").strip().capitalize()
                #Mientras el dia no esté en el diccionario de dias con lluvia o sea el mismo que el primer dia, pedimos otro dia
                while dia2 not in pluja_per_dia or dia1 == dia2:
                    #Si el dia no está en el diccionario, imprimimos un mensaje de error
                    if dia2 not in pluja_per_dia:
                        print("El dia introduït no es troba a la llista.")
                    #Si el dia es el mismo que el primer dia, imprimimos un mensaje de error
                    else:
                        print("Has d'escollir un altre dia diferent.")
                    dia2 = input("Introdueix un dia de la setmana: ").strip().capitalize()
                print()
                #Obtenemos los conjuntos de ciudades donde ha llovido para cada dia
                ciutats1 = pluja_per_dia[dia1]
                ciutats2 = pluja_per_dia[dia2]
                
                #Creamos conjuntos de ciudades en minuscula para poder comparar sin importar mayusculas o minusculas
                ciutats1_lower = {c.lower() for c in ciutats1}
                ciutats2_lower = {c.lower() for c in ciutats2}
                #Creamos un conjunto con todas las ciudades del diccionario de precipitaciones por ciudad
                todas_ciudades = set(pluja_per_ciutat.keys())
                
                #Imprimimos los resultados de la comparación de ciudades donde ha llovido entre los dos dias
                print(f"El {dia1} ha plogut a: {ciutats1_lower}")
                print(f"El {dia2} ha plogut a: {ciutats2_lower}")
                #Imprimimos las ciudades donde ha llovido en ambos dias, en el primer dia pero no en el segundo, en uno de los dos dias, y en ninguno de los dos dias
                print("Ciutats on ha plogut els dos dies:", ciutats1_lower & ciutats2_lower)
                print("Ciutats on ha plogut el primer dia pero no el segon:", ciutats1_lower - ciutats2_lower)
                print("Ciutats on ha plogut nomes un dels dos dies:", ciutats1_lower ^ ciutats2_lower)
                print("Ciutats on no ha plogut cap dels dos dies:", todas_ciudades - (ciutats1_lower | ciutats2_lower))
                print()
            
            #Opció 8. Màxim, mínim i mitjana d'humitat 
            elif opcion == 8:
                #Imprime el titulo
                print(f'{"Ciutat":<30}{"Màxim (%)":<11}{"Mínim (%)":<11}{"Mitjana (%)":<11}')
                print("-" * 63)
                
                #Creamos una lista vacia para guardar todas las humedades de todas las ciudades
                todas_las_humedades = []
                #Creamos variables para guardar el maximo y minimo global de humedad
                max_global = 0
                min_global = 100
                #Recorremos cada diccionario de la lista de diccionarios
                for c in dades_meteorologiques:
                    #Guardamos la lista de humedades de la ciudad actual
                    humitat_ciutat= c['Humitat']
                    #Calculamos el maximo, minimo y media de la humedad de la ciudad actual
                    humitat_max= max(humitat_ciutat)
                    humitat_min= min(humitat_ciutat)
                    humitat_mitjana= sum(humitat_ciutat) / len(humitat_ciutat)
                    #Imprimimos la ciudad y sus valores de humedad
                    print(f"{c['Ciutat']:<30}{humitat_max:<11}{humitat_min:<11}{humitat_mitjana:<11.2f}")
                    #Añadimos las humedades de la ciudad actual a la lista de todas las humedades
                    todas_las_humedades.extend(humitat_ciutat)
                    
                    #Buscamos el maximo y minimo global de humedad comparando con los valores actuales
                    if humitat_max > max_global:
                        max_global = humitat_max
                    if humitat_min < min_global:
                        min_global = humitat_min
                #Imprimimos una linea
                print("-" * 63)
                #Calculamos la media global de humedad
                mitjana_global = sum(todas_las_humedades) / len(todas_las_humedades)
                #Imprimimos los valores globales de humedad, incluyendo el máximo, mínimo y media con dos decimales
                print("Humitat global:")
                print(f"Màxim: {max_global} %")
                print(f"Mínim: {min_global} %")
                print(f"Mitjana: {mitjana_global:.2f} %")
                print()
                
            #Opció 9. Ciutats amb temperatures superiors a un llindar
            elif opcion == 9:
                #Pedimos al usuario que introduzca un umbral de temperatura entre 5 y 25, y validamos la entrada
                llindar = input("Introdueix un llindar (entre 5 i 25): ").strip()
                #Mientras la entrada no sea un número o no esté entre 5 y 25, pedimos otra entrada
                while not llindar.isdigit() or not (5 <= int(llindar) <= 25):
                    #Si la entrada no es un número o no está entre 5 y 25, imprimimos un mensaje de error
                    print("Valor incorrecte.")
                    #Volvemos a pedir la entrada
                    llindar = input("Introdueix un llindar (entre 5 i 25): ").strip()
                #Convertimos la entrada a un número entero
                llindar = int(llindar)

                #Creamos una lista de ciudades que han superado el umbral de temperatura en algún día, usando una list comprehension
                ciutats_superades = [c["Ciutat"] for c in dades_meteorologiques if any(t > llindar for t in c["Temperatures"])]
                
                #Imprimimos las ciudades que han superado el umbral de temperatura, junto con la cantidad de ciudades encontradas
                print(f"Ciutats que han superat els {llindar} ºC algun dia ({len(ciutats_superades)}):")
                print(", ".join(ciutats_superades))
                print()
                
            #Opció 10. Comparar temperatures entre dues ciutats
            elif opcion == 10:
                #Flag para controlar la validez de la entrada de la primera ciudad
                valida = False
                #Mientras la primera ciudad no sea válida, pedimos al usuario que introduzca una ciudad
                while not valida:
                    #Pedimos al usuario que introduzca la primera ciudad y la convertimos a minuscula y quitamos espacios al principio y al final
                    entrada = input("Introdueix la primera ciutat: ").strip().lower()
                    #Buscamos la ciudad en la lista de diccionarios y guardamos su posición si se encuentra
                    for i in range(len(dades_meteorologiques)):
                        #Si la ciudad introducida coincide con el nombre de la ciudad en el diccionario, guardamos su posición y marcamos la entrada como válida
                        if dades_meteorologiques[i]["Ciutat"].lower() == entrada:
                            pos1 = i
                            valida = True
                    #Si la ciudad no se encuentra en la lista, imprimimos un mensaje de error
                    if not valida:
                        print("Error: aquesta ciutat no està a la llista.")
                
                #Flag para controlar la validez de la entrada de la segunda ciudad
                valida = False
                #Mientras la segunda ciudad no sea válida, pedimos al usuario que introduzca una ciudad
                while not valida:
                    #Pedimos al usuario que introduzca la segunda ciudad y la convertimos a minuscula y quitamos espacios al principio y al final
                    entrada = input("Introdueix la segona ciutat: ").strip().lower()
                    trobada = False
                    #Buscamos la ciudad en la lista de diccionarios y guardamos su posición si se encuentra
                    for i in range(len(dades_meteorologiques)):
                        if dades_meteorologiques[i]["Ciutat"].lower() == entrada:
                            trobada = True
                            #Si la ciudad introducida coincide con el nombre de la ciudad en el diccionario, comprobamos si es la misma que la primera ciudad, si lo es, imprime un mensaje de error
                            if i == pos1:
                                print("Error: has de triar una ciutat diferent.")
                            #Si no es la misma ciudad, guardamos su posición y marcamos la entrada como válida
                            else:
                                pos2 = i
                                valida = True
                    #Si la ciudad no se encuentra en la lista, imprimimos un mensaje de error
                    if not trobada:
                        print("Error: aquesta ciutat no està a la llista.")

                print()
                #Obtenemos los nombres de las ciudades y sus listas de temperaturas usando las posiciones guardadas
                c1 = dades_meteorologiques[pos1]["Ciutat"]
                c2 = dades_meteorologiques[pos2]["Ciutat"]
                t1 = dades_meteorologiques[pos1]["Temperatures"]
                t2 = dades_meteorologiques[pos2]["Temperatures"]

                #Imprimimos los nombres de las ciudades y sus listas de temperaturas
                print(f"{c1}: " + ", ".join(f"{t} ºC" for t in t1))
                print(f"{c2}: " + ", ".join(f"{t} ºC" for t in t2))
                print()
                #Comparamos las temperaturas de cada día y imprimimos cuál ciudad ha tenido más frío o más calor, o si han tenido la misma temperatura
                for i in range(len(dies)):
                    #Si la temperatura de la primera ciudad es menor que la de la segunda ciudad, imprimimos que ha hecho más frío en la primera ciudad
                    if t1[i] < t2[i]:
                        print(f"{dies[i]}: a {c1} ha fet més fred que a {c2} ({t1[i]} ºC / {t2[i]} ºC)")
                    #Si la temperatura de la primera ciudad es mayor que la de la segunda ciudad, imprimimos que ha hecho más calor en la primera ciudad
                    elif t1[i] > t2[i]:
                        print(f"{dies[i]}: a {c1} ha fet més calor que a {c2} ({t1[i]} ºC / {t2[i]} ºC)")
                    #Si las temperaturas son iguales, imprimimos que han tenido la misma temperatura
                    else:
                        print(f"{dies[i]}: a {c1} i a {c2} ha fet la mateixa temperatura ({t1[i]} ºC)")
                print()
        
        #Si la opción no está entre 0 y 10, imprimimos un mensaje de error
        else: 
            print("Error: has d'escriure un número entre 0 i 10.")
            print()
    #Si la opción no es un número, imprimimos un mensaje de error
    else:
        print("Error: has d'escriure un número entre 0 i 10.")
        print()
