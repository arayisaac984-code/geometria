import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from itertools import combinations, product

def ejecutar_programa():
    while True:
        print("\n--- Generador de figuras ---")
        print("2D: 1. Cuadrado, 2. Círculo")
        print("3D: 3. Cubo, 4. Esfera, 5. Pirámide")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        # Configuración del lienzo
        if opcion in ["3", "4", "5"]:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_zlim(0, 10)
        elif opcion in ["1", "2"]:
            fig, ax = plt.subplots()
            ax.set_xlim(0, 10); ax.set_ylim(0, 10)
            ax.set_aspect('equal')
        else:
            print("Opción no válida.")
            continue

        # Lógica de dibujo
        if opcion == "1":
            ax.add_patch(plt.Rectangle((3, 5), 2, 3, color="green"))
            ax.set_title("Cuadrado 2D")
        
        elif opcion == "2":
            try:
                # Pedimos los datos al usuario
                print("Configuración del Círculo:")
                x = float(input("Posición X (0-10): "))
                y = float(input("Posición Y (0-10): "))
                radio = float(input("Radio: "))
                
                if radio <= 0:
                    print("Error: El radio debe ser mayor a 0.")
                    plt.close(fig)
                    continue
                
                ax.add_patch(plt.Circle((x, y), radio, color="blue"))
                ax.set_title(f"Círculo en ({x}, {y}) con radio {radio}")
                
            except ValueError:
                print("Error: Debes ingresar números válidos.")
                plt.close(fig)
                continue
                
        elif opcion == "3":
            r = [2, 6]
            for s, e in combinations(np.array(list(product(r, r, r))), 2):
                if np.sum(np.abs(s-e)) == r[1]-r[0]:
                    ax.plot3D(*zip(s, e), color="red")
            ax.set_title("Cubo 3D")
        elif opcion == "4":
            u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
            ax.plot_wireframe(5 + 3*np.cos(u)*np.sin(v), 5 + 3*np.sin(u)*np.sin(v), 5 + 3*np.cos(v), color="purple")
            ax.set_title("Esfera 3D")
        elif opcion == "5":
            v = np.array([[2,2,0], [8,2,0], [8,8,0], [2,8,0], [5,5,8]])
            ax.add_collection3d(Poly3DCollection([v[[0,1,4]], v[[1,2,4]], v[[2,3,4]], v[[3,0,4]]], alpha=0.5, color='orange'))
            ax.set_title("Pirámide 3D")

        plt.show()

ejecutar_programa()