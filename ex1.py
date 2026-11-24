from datetime import date 

def mostar_menu():  
    """Mostra les cinc opcions del menú principal."""
    print("Funcions 1")
    print("=" * 50)
    print("1. Multiplica")
    print("2. Anys 2000")
    print("3. Gira del revés")
    print("4. Triangle de Pascal")
    print("5. Sortir")
        
def multiplicac(a,b):
    """Multiplica els dos enters rebuts i mostra l'operació amb el resultat."""
    print(f"{a} x {b} = {a * b}") 

def anys_2000():
    """Demana un any vàlid i mostra els anys transcorreguts des del 2000."""
    any_actual = date.today().year
    Valid= False
    while not Valid:
        any= input(f"Introdueix un any entre 2000 i {any_actual}: ")
        if any.isdigit():
            any= int(any)
            if 2000 <= any <= any_actual:
                print(f"Des del 2000 han passat {any - 2000} anys")
                Valid= True
            else:
                print(f"L'any ha de ser un número entre 2000 i {any_actual}.")
        else:
            print(f"L'any ha de ser un número entre 2000 i {any_actual}.")
def gira_reves():
    """Demana una cadena i la mostra del revés amb un bucle."""
    cadena= input("Introdueix una cadena: ")
    cadena_invertida= ""
    for caracter in cadena:
        cadena_invertida= caracter + cadena_invertida
    print(cadena_invertida)

def triangle_pascal():
    """Demana el nombre de files (entre 2 i 10) i imprimeix el triangle de Pascal."""
    Valid= False
    filas= 0
    while not Valid:
        n_filas= input(f"Nombre de filas (entre 2 i 10): ")
        if n_filas.isdigit():
            n_filas= int(n_filas)
            if 2 <= n_filas <= 10:
                filas= n_filas
                Valid= True
            else:
                print("Ha de ser un número entre 2 i 10.")
        else:
            print("Ha de ser un número entre 2 i 10.")

    numeros = [1]

    for i in range(1, filas + 1):
        if i > 1:
            nueva = [1]

            for j in range(len(numeros) - 1):
                nueva.append(numeros[j] + numeros[j + 1])

            nueva.append(1)
            numeros = nueva

        print(" " * (filas - i), end="")
        print(*numeros)
            
def main():
    """Mostra el menú i executa l'opció escollida fins que l'usuari tria sortir."""
    Sortir= False
    while not Sortir:
        mostar_menu()
        opcion= input("Escull una opció: ").strip()
        if opcion == "1":
            Valid= False
            while not Valid:
                numero1= input("Primer número: ").strip()
                if numero1.removeprefix("-").isdigit():
                    a= int(numero1)
                    Valid= True
                else:
                    print("Ha de ser un enter.")
            
            Valid= False
            while not Valid:
                numero2= input("Segon número: ").strip()
                if numero2.removeprefix("-").isdigit():
                    b= int(numero2)
                    Valid= True
                else:
                    print("Ha de ser un enter.")
            multiplicac(a,b)
        elif opcion == "2":
            anys_2000()
        elif opcion == "3":
            gira_reves()
        elif opcion == "4":
            triangle_pascal()
        elif opcion == "5":
            print("Sortint del menú")
            Sortir = True
                    
        else: 
                print("Opció incorrecta. Ha de ser un número de l'1 al 5.")


if __name__ == "__main__": main()

        
            