import random
import csv
nombres=[
    "Juan Perez",
     "Maria Garcia",
     "Carlos Lopez",
     "Ana Martinez",
     "Pedro Rodriguez",
     "Laura Hernandez",
     "Miguel Sanchez",
     "Isabel Gomez",
     "Francisco Diaz",
     "Elena Fernandez"
]
sueldo_trabajadores=[]

with open("sueldos_trabajos.csv", "w") as archivo:
    archivo.write("| nombre empleado | sueldo base | descuento salud | descuento afp | sueldo liquido\n")
def sueldo_aleatorio():
    sueldo_trabajadores.clear()
    for numero in range(len(nombres)):
        sueldo_trabajadores.append({"nombre": nombres[numero], "sueldo": random.randint(300000, 2500000)})
        return "finalizado"
    
def clasificar_sueldos():
    menor_800000=[trabajador for trabajador in sueldo_trabajadores if trabajador["sueldo"]<800000]
    de_800000_2m=[trabajador for trabajador in sueldo_trabajadores if 800000<=trabajador["sueldo"]<=2000000]
    superior_2m=[trabajador for trabajador in sueldo_trabajadores if trabajador["sueldo"]>2000000]
    
    print("sueldos menores de $800.000")
    print(f"Total: {len(menor_800000)}")
    for trabajador in menor_800000:
        print(f"{trabajador["nombre"]}: ${trabajador["sueldo"]}")
    print()
    
    print("sueldos entre $800.000 y $2.000.000")
    print (f"Total: {len(de_800000_2m)}")
    for trabajador in de_800000_2m:
        print(f"{trabajador["nombre"]}: ${trabajador["sueldo"]}")
        print()
        
    print("sueldo superior a $2.000.000")
    print(f"Total: {len(superior_2m)}")
    for trabajador in superior_2m:
        print(f"{trabajador["nombre"]}: ${trabajador["sueldo"]}")
        print()
    
total_sueldos=sum(trabajador ["sueldo"] for trabajador in sueldo_trabajadores)
print(f"TOTAL SUELDOS: ${total_sueldos}")

def estadisticas_total():
    total=sum(trabajador["sueldo"] for trabajador in sueldo_trabajadores)
    maximo_sueldo=max(sueldo_trabajadores, key=lambda x: x["sueldo"])
    minimo_sueldo=min(sueldo_trabajadores, key=lambda x: x["sueldo"])
    promedio=total/len(nombres)
    
    print("sueldo mas alto: ", maximo_sueldo)
    print("sueldo mas bajo: ", minimo_sueldo)
    print("promedio de sueldos: ", promedio)
    
def reporte_sueldos():
    with open ("sueldos_trabajos.csv", "a") as archivo:
        for sueldos in sueldo_trabajadores:
            descuento=0.07*sueldos["sueldo"]
            desafp=0.012*sueldos["sueldo"]
            sueldo_liquido=sueldos["sueldo"]-descuento-desafp
            archivo.write(f"{sueldos["nombre"]},-{sueldos["sueldo"]},-{descuento}-{desafp}-{sueldo_liquido}\n")
            
while True:
    print("1. asignar sueldo aleatorio.")
    print("2. clasificar sueldos.")
    print("3. ver estadisticas.")
    print("4. reporte de sueldos.")
    print("5. salir del programa.")
    try:
        menu=int(input("seleccione una opcion: "))
    except ValueError:
        print("seleccion invalida, por favor selecione una opcion del menu")
    else:
        match menu:
                case 1:
                    sueldo_aleatorio()
                    print("se ha generado el proceso aleatorio")
                case 2:
                    clasificar_sueldos()
                    input("se ha procesado con exito")
                case 3:
                    estadisticas_total()
                    input("se ha procesado con exito")
                case 4:
                    reporte_sueldos()
                    input("se ha procesado con exito")
                case 5:
                    print("finalizando programa...| desarrollado por Hadde Atenas | rut 20.880.433-2 |")
                    break  
            