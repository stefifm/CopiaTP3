import copia

print("Programa principal del TP3")




def principal():
    competidores = []

    print("Lista de participantes que estarán en competencia\n")

    lista_participantes = ["Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express"]

    for i in range(len(lista_participantes)):
        print(lista_participantes[i])

    print("\nHora de cargar los participantes en los arreglos\n")
    opcion = int(input("1 para hacer la carga manual. 2 para carga "
                       "automática: "))
    if opcion == 1:
        copia.carga_manual(competidores)
    else:
        copia.carga_automatica(competidores)
        print("Hecho, Ya están cargado los competidores.")
    print("Presione <Enter> para continuar")
    input()

    print("\nLista ordenada de los competidores\n")
    copia.orden_sort(competidores)
    copia.mostrar_participantes(competidores)

    print("Estádistica cantidad de participantes por continente\n")
    copia.estadistica_continente(competidores)

    print("Presione <Enter> para empezar con la competencia")
    input()

    print("Largamos con los octavos de final")
    print("Presione <Enter> para ver los enfrentamientos con sus puntos")
    input()

    print("\nRonda de octavos\n")
    copia.fixture(competidores)

    print("\nEstadística promedio de puntos en octavos")
    prom_octavos = copia.estadistica_promedio_ronda(competidores)
    print("Promedio de puntos en octavos:",prom_octavos)

    print("Vamos con otro <Enter> para continuar con los cuartos de final")
    input()


    print("Bandera verde para los cuartos de final")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de Cuartos de Final\n")
    cuartos = copia.ganador(competidores)
    copia.fixture(cuartos)

    print("\nEstadística promedio de puntos en cuartos:")
    prom_cuartos = copia.estadistica_promedio_ronda(cuartos)
    print("Promedio de puntos en cuartos:",prom_cuartos)

    print("Vamos con otro <Enter> para entrar a las semifinales")
    input()

    print("¡¡¡Aquí están las semis!!!")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de semifinales\n")
    semis = copia.ganador(cuartos)
    copia.fixture(semis)

    print("\nEstadística promedio de puntos en semifinales")
    prom_semis = copia.estadistica_promedio_ronda(semis)
    print("Promedio de puntos en semifinales:",prom_semis)

    print("Vamos con otro <Enter> para la definición del tercer puesto")
    input()

    print("Aquí viene el tercer puesto")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de Tercer Puesto\n")
    tercer = copia.tercer(semis)
    copia.fixture(tercer)
    tercer_puesto = copia.tercero(tercer)
    print("\nTercer puesto:",copia.to_string(tercer_puesto))

    print("¡¡¡LLegamos a la final!!! <Enter> para la definición")
    input()

    print("¡¡¡La gran final!!!")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nGran Final\n")
    final = copia.final(semis)
    copia.fixture(final)
    primero, segundo = copia.top2(final)

    print("\n!!!!Y aquí están los campeones y subcampeones!!!!\n")
    print("Campeón:",copia.to_string(primero))
    print("Subcampeón:",copia.to_string(segundo))


    print("Se acabó..... ")
    print("\nPresione <Enter> para ver el nuevo ranking....")
    input()

    print("\nNuevo Ranking tras la competencia\n")
    new_list = copia.nuevo_arreglo(primero, segundo, tercer_puesto,
                                   competidores)
    copia.orden_sort(new_list)
    copia.mostrar_participantes(new_list)





if __name__ == "__main__":
    principal()