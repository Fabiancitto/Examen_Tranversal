import os
os.system("cls")

ListaEntradas = []
UbicacionD = list(range(1, 101))
UbicacionV = []
ListaRun = []


print("Bienvenido a creativos.cl")
nom = input("Ingrese Su Nombre: ")
ape = input("Ingrese Su Apellido: ")
print("10/07/2023")

menu = """-----------------------------
1. Comprar Entradas
2. Mostrar Ubicaciones Disponibles
3. Ver Listado De Asistentes
4. Mostrar ganancias totales
5. Salir
-----------------------------
Seleccione Opcion:
"""
opc = int(input(menu))

def EntradasF():
    while True:
        try:
            entra = int(input("Ingrese cantidad de entradas: "))
            if entra <=3 and entra >=1:
                for i in range(1, 101):
                    if i in UbicacionD:
                        print(f"Asiento {i}: Disponible")
                    elif i in UbicacionV:
                        print(f"Asiento {i}: Vendido")
                for i in range(entra):
                    ubi = int(input("Seleccione una ubicación disponible: "))
                while ubi not in UbicacionD:
                    print("Ubicación no disponible. Por favor, seleccione otra.")
                    ubi = int(input("Seleccione una ubicación disponible: "))
                ListaEntradas.append(ubi) 
                UbicacionD.remove(ubi)
                UbicacionV.append(ubi)
            else:
                print("La Cantidad Ingresada No Es Valida") 
        except:
            print("Ocurrio una excepcion")


def MostrarF():
    for i in range(1, 101):
        if i in UbicacionD:
            print(f"Asiento {i}: Disponible")
        elif i in UbicacionV:
            print(f"Asiento {i}: Vendido")

def AsistenteF():
    print(ListaRun)

def GanaciasF():
    pla = 0
    gold = 0
    sil = 0
    for ubicacion in ListaEntradas:
        if ubicacion >= 1 or ubicacion <= 20:
            pla += 1
        elif ubicacion >= 21 or ubicacion <= 50:
            gold += 1
        elif ubicacion >= 51 or ubicacion <= 100:
            sil += 1
    run = input("Ingrese su RUN sin guiones ni puntos: ")
    ListaRun.append(run)
    print(f"Se han comprado {UbicacionV}")
    print(f"""
    Entrada     |       Cantidad      | Precio
    --------------------------------------------------
    Platinum    |       {pla}         | {pla*120000}
    Gold        |       {gold}        | {gold*80000}
    Silver      |       {sil}         | {sil*50000}
    --------------------------------------------------
    """)
    print(f"Su RUN: {run}")
    print("¡Disfrute del evento!")


if opc == 2:
    MostrarF()
elif opc == 3:
    AsistenteF()
elif opc == 1:
    EntradasF()
elif opc == 4:
    GanaciasF()
elif opc == 5:
    print(f"Muchas Gracias {nom} {ape} por visitarnos")
    print("10/07/2023") 
else:
    print("Error al ingresar")