def mostrar_menu():
    
    print("Funcions 2")
    print("====================")
    print("1. Comptar majúscules i minúscules")
    print("2. Any de traspàs")
    print("3. Dies del mes")
    print("4. Número perfecte")
    print("5. Números perfectes fins a 10000  (repte)")
    print("0. Sortir")

def introduir_int_segur(missatge, minim= None, maxim= None):
    Valid= False
    Valor= 0
    while not Valid:
        dato= input(missatge)
        if dato.isdigit():
            Valor= int(dato)
            if minim is not None and Valor < minim:
                print("Introdueix un número més gran.")
            elif maxim is not None and Valor >  maxim:
                print("Introdueix un número més petit")
            else:
                Valid= True
        else:
            print("Has d'introduir un número enter.")
    return Valor

def comptar_majuscules_minuscules(cadena):
    """Compta les lletres majúscules i minúscules d'una cadena."""
    
    majuscules= 0
    minuscules= 0
    
    for caracter in cadena:
        if caracter.isupper():
            majuscules += 1
        elif caracter.islower():
            minuscules += 1
    return (majuscules, minuscules)

def es_any_traspas(a):
    """
    Determina si un any és de traspàs.
 
    Regles:
    - Divisible per 4, però no per 100,
    - excepte si és divisible per 400.
 
    Args:
        a (int): Any a comprovar
 
    Returns:
        bool: True si és any de traspàs, False en cas contrari
 
    Exemples:
        >>> es_any_traspas(2000)
        True
        >>> es_any_traspas(1900)
        False
        >>> es_any_traspas(2024)
        True
    """
    # TODO: Implementar la funció
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

def comptar_dies_mes(mes, a):
    """Retorna el nombre de dies d'un mes en un any determinat."""
    
    dies_per_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    if mes == 2 and es_any_traspas(a):
        return 29
    elif mes == 2 and not es_any_traspas(a):
        return 28
    else:
        return dies_per_mes[mes - 1] 
    
def es_num_perfecte(numero):
    """
    Comprova si un número és perfecte.
 
    Un número perfecte és igual a la suma dels seus divisors
    positius propis (excloent el número mateix).
 
    Args:
        numero (int): Número a comprovar (enter positiu)
 
    Returns:
        bool: True si és perfecte, False en cas contrari
 
    Exemples:
        >>> es_num_perfecte(6)     # 1+2+3 = 6
        True
        >>> es_num_perfecte(28)    # 1+2+4+7+14 = 28
        True
        >>> es_num_perfecte(12)
        False
    """
    # TODO: Implementar la funció
    if numero <= 1:
        return False
    suma_divisor= 0
    
    for i in range (1, (numero // 2) + 1):
        if numero % i == 0:
            suma_divisor += i
    return suma_divisor == numero

def main():
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = introduir_int_segur("Escull una opció: ", 0, 5)
        if opcion == 1:
            text= input("Introdueix una cadena: ")
            maj, min = comptar_majuscules_minuscules(text)
            print(f"Majuscules: {maj} | Minuscules: {min}")
            
        elif opcion == 2:
            any = introduir_int_segur("Introdueix un any: ", 1)
            if es_any_traspas(any):
                print(f"L'any {any} és de traspàs.")
            else:
                print(f"L'any {any} no és de traspàs.")
        
        elif opcion == 3:
            mes = introduir_int_segur("Mes (1-12): ", 1, 12)
            anys = introduir_int_segur("Any: ", 1)
            dies = comptar_dies_mes(mes, anys)
            print(f"El mes {mes} de l'any {anys} té {dies} dies.")
        elif opcion == 4:
            num = introduir_int_segur("Introdueix un número enter positiu: ", 1)
            if es_num_perfecte(num):
                print(f"El número {num} és perfecte.")
            else:
                print(f"El número {num} no és perfecte.")
        elif opcion == 5:
            print("Números perfectes fins a 10000:")
            for n in range(1, 10001):
                if es_num_perfecte(n):
                    print(n)
        elif opcion == 0:
            print("Sortient del programa")
            
if __name__ == "__main__": main()