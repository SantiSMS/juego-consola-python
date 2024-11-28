import random
from clases.jugador import Jugador
from clases.enemigo import Enemigo


def main():
    nombre_jugador = input("Bienvenido! Nombre?")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Topo", 50, 10),
        Enemigo("Topardi", 30, 5),
        Enemigo("Pijudo", 70, 15),
    ]
    enemigos_derrotados = [                                                                                                                 ]

    print("Comienza el juego")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue    # le estamos pidiendo que saltee el loop

        print(f"Tu enemigo es: {enemigo_actual.nombre}")

        while enemigo_actual.salud >= 0:
            accion = input("Quieres atacar o huir?").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Has atacado a {enemigo_actual.nombre} y has causado {dano_jugador} de daño"
                )
                enemigo_actual.recibir_dano(
                    dano_jugador
                )  # le paso al enemigo actual el daño que le hice

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"El {enemigo_actual.nombre} te ha atado y hecho {dano_enemigo} de daño"
                    )
                    jugador.recibir_dano(
                        dano_enemigo
                    )  # le paso al jugador el daño que le hicieron

            elif accion == huir:
                print("Te cagaste!")
                break

        if jugador.salud <= 0:
            print("Perdiste")
            break

        if enemigo_actual.salud <=0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual) 

        jugador.ganar_experiencia(20)

        continuar = input("Seguis? s/n").lower()

        if continuar != "s":
            print("Cagón")
            break

    if not enemigos:
        print("Te los cogiste a todos")

if __name__== "__main__":   # nos asegura que solo podamos ejecutar este script desde el programa principal
    main()


