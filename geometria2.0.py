import turtle
import sys

# Configuramos la tortuga globalmente
try:
    pincel = turtle.Turtle()
    pincel.speed(5)
except turtle.Terminator:
    print("Error al iniciar la ventana de dibujo.")

def preparar_lienzo():
    """Limpia y centra la tortuga evitando errores si la ventana se cerró."""
    try:
        pincel.clear()
        pincel.penup()
        pincel.home()
        pincel.pendown()
    except turtle.Terminator:
        print("\n[!] La ventana de dibujo estaba cerrada. Reabriéndola...")
        reinstanciar_tortuga()

def reinstanciar_tortuga():
    """Intenta recuperar la tortuga si el usuario cerró la ventana."""
    global pincel
    turtle.Screen().clear()
    pincel = turtle.Turtle()
    pincel.speed(5)

def dibujar_cuadrado():
    try:
        preparar_lienzo()
        for _ in range(4):
            pincel.forward(100)
            pincel.left(110)
        print("\n[✓] Cuadrado dibujado con éxito.")
    except Exception as e:
        print(f"\n[!] Error al dibujar: {e}")

def dibujar_triangulo():
    try:
        preparar_lienzo()
        for _ in range(3):
            pincel.forward(100)
            pincel.left(120)
        print("\n[✓] Triángulo dibujado con éxito.")
    except Exception as e:
        print(f"\n[!] Error al dibujar: {e}")

def dibujar_circulo():
    try:
        preparar_lienzo()
        pincel.circle(50)
        print("\n[✓] Círculo dibujado con éxito.")
    except Exception as e:
        print(f"\n[!] Error al dibujar: {e}")

def menu():
    while True:
        print("\n" + "="*30)
        print("  GENERADOR DE FIGURAS PRO")
        print("="*30)
        print("1. Dibujar Cuadrado")
        print("2. Dibujar Triángulo")
        print("3. Dibujar Círculo")
        print("4. Limpiar Lienzo")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ").strip()

        # VALIDACIÓN 1: Entrada vacía o espacios
        if not opcion:
            print("[!] No ingresaste nada. Intenta de nuevo.")
            continue

        # VALIDACIÓN 2: Entrada no numérica
        if not opcion.isdigit():
            print(f"[!] '{opcion}' no es un número válido.")
            continue

        # CONTROL DE OPCIONES
        if opcion == "1":
            dibujar_cuadrado()
        elif opcion == "2":
            dibujar_triangulo()
        elif opcion == "3":
            dibujar_circulo()
        elif opcion == "4":
            try:
                pincel.clear()
                print("\n[!] Lienzo limpio.")
            except:
                print("\n[!] No hay lienzo que limpiar.")
        elif opcion == "5":
            print("¡Cerrando aplicación de forma segura!")
            try:
                turtle.bye()
            except:
                pass
            break
        else:
            print(f"[!] La opción {opcion} no está en el menú.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario (Ctrl+C).")
        sys.exit()