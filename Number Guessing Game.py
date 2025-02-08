import random
import time

# Variable global para rastrear el mejor puntaje
mejor_puntaje = float('inf')

def jugar():
    global mejor_puntaje
    
    print("\n¡Bienvenido al Juego de Adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    # Solicitar al usuario que seleccione la dificultad
    print("\nPor favor, selecciona el nivel de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (5 intentos)")
    print("3. Difícil (3 intentos)")
    
    while True:
        try:
            eleccion = int(input("Ingresa tu elección (1, 2 o 3): "))
            if eleccion in [1, 2, 3]:
                break
            else:
                print("Por favor, ingresa un número válido (1, 2 o 3).")
        except ValueError:
            print("Por favor, ingresa un número válido (1, 2 o 3).")
    
    # Asignar el número de intentos según la dificultad
    if eleccion == 1:
        intentos_maximos = 10
        print("\n¡Genial! Has seleccionado el nivel Fácil.")
    elif eleccion == 2:
        intentos_maximos = 5
        print("\n¡Genial! Has seleccionado el nivel Medio.")
    else:
        intentos_maximos = 3
        print("\n¡Genial! Has seleccionado el nivel Difícil.")
    
    print(f"Tienes {intentos_maximos} intentos para adivinar el número.")
    
    # Iniciar el temporizador
    start_time = time.time()
    
    # Iniciar el juego
    intentos = 0
    while intentos < intentos_maximos:
        intentos += 1
        try:
            guess = int(input("\nIngresa tu suposición: "))
            if guess < 1 or guess > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if guess == numero_secreto:
            end_time = time.time()
            tiempo_total = round(end_time - start_time, 2)
            print(f"\n¡Felicidades! ¡Adivinaste el número correcto en {intentos} intentos!")
            print(f"¡Tardaste {tiempo_total} segundos en adivinar el número!")
            
            # Actualizar el mejor puntaje
            if intentos < mejor_puntaje:
                mejor_puntaje = intentos
                print(f"¡Nuevo récord! Tu mejor puntaje es ahora {mejor_puntaje} intentos.")
            break
        elif guess < numero_secreto:
            print("Incorrecto. El número es mayor que", guess)
        else:
            print("Incorrecto. El número es menor que", guess)
        
        # Dar una pista después de 3 intentos fallidos
        if intentos == 3:
            if numero_secreto % 2 == 0:
                print("Pista: El número es par.")
            else:
                print("Pista: El número es impar.")
        
        if intentos == intentos_maximos:
            print(f"\n¡Lo siento! Te has quedado sin intentos. El número era {numero_secreto}.")

def main():
    while True:
        jugar()
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("\n¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()