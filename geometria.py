import turtle
def dibujar_cuadrado():
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    print("\n[✓] Cuadrado dibujado.")

def dibujar_triangulo():
    t = turtle.Turtle()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    print("\n[✓] Triángulo dibujado.")

def dibujar_circulo():
    t = turtle.Turtle()
    t.circle(50)
    print("\n[✓] Círculo dibujado.")

def menu():
    while True:
        print("\n--- GENERADOR DE FIGURAS ---")
        print("1. Dibujar Cuadrado")
        print("2. Dibujar Triángulo")
        print("3. Dibujar Círculo")
        print("4. Limpiar pantalla")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ")

        if opcion == "1":
            dibujar_cuadrado()
        elif opcion == "2":
            dibujar_triangulo()
        elif opcion == "3":
            dibujar_circulo()
        elif opcion == "4":
            turtle.clearscreen()
            print("\n[!] Pantalla limpia.")
        elif opcion == "5":
            print("¡Hasta luego!")
            turtle.bye() # Cierra la ventana de dibujo
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()