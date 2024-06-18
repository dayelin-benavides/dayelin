trabajadores=[]

def valido(texto):
    return texto.isalpha()

def registrar_trabajador():
    while True:
        nombre = input("Ingrese nombre del trabajador: ")
        if nombre and valido(nombre):
            break
        print("No puede contener numeros. Intente otra vez.")

    while True:
        apellido = input("Ingrese apellido del trabajador: ")
        if apellido and valido(apellido):
            break
        print("No puede contener numeros. Intente otra vez.")

    while True:
        try:
            print("Seleccione un cargo: ")
            print("1.- CEO.")
            print("2.- Desarrollador.")
            print("3.- Analista.")
            cargo = int(input("Ingrese numero segun el cargo: "))
            if cargo==1:
                cargo="CEO"
                print("Usted eligio CEO.")
                break
            elif cargo==2:
                cargo="Desarrollador"
                print("Usted eligio Desarrollador.")
                break
            elif cargo==3:
                cargo="Analista"
                print("Usted eligio Analista.")
                break
            else:
                print("ERROR. Debe ser un numero del menu.")
        except ValueError:
            print("Ingrese caracter numerico.")

    while True:
        try:
            sueldoBruto = int (input("Ingrese el sueldo bruto: "))
            if sueldoBruto > 0:
                break
            else:
                print("El sueldo debe ser mayor a 0. Intente otra vez.")
        except ValueError:
            print("Solo puede contener numeros. Intente otra vez.")
    
    descuentoSalud=round(0.07*sueldoBruto)
    descuentoAFP=round(0.12*sueldoBruto)
    liquido=round(sueldoBruto-descuentoSalud-descuentoAFP)
    trabajadores.append((nombre,apellido,cargo,sueldoBruto,descuentoSalud,descuentoAFP,liquido))

def listarTrabajadores():
    for trabajador in trabajadores:
        print(f"Nombre: {trabajador[0]}, Apellido: {trabajador[1]}, Cargo: {trabajador[2]}, Sueldo Bruto: {trabajador[3]}, Desc. Salud: {trabajador[4]}, Desc. AFP: {trabajador[5]} Líquido a Pagar: {trabajador[6]}")

def imprimir_planilla():
    with open("Planilla.txt", "w") as archivo:
        for trabajador in trabajadores:
            archivo.write(f"Nombre: {trabajador[0]}, Apellido: {trabajador[1]}, Cargo: {trabajador[2]}, Sueldo Bruto: {trabajador[3]}, Desc. Salud: {trabajador[4]}, Desc. AFP: {trabajador[5]} Líquido a Pagar: {trabajador[6]}\n")


def salirDelPrograma():
    print("Saliendo...")
    exit()

opcion=9
while opcion!=4:
    try:
        print("1.- Registrar trabajado.")
        print("2.- Listar los trabajadores.")
        print("3.- Imprimir planilla de sueldos.")
        print("4.- Salir.")
        
        opcion = int(input("Selecciones una opcion: "))

        if opcion == 1:
            registrar_trabajador()
        elif opcion == 2:
            listarTrabajadores()
        elif opcion == 3:
            imprimir_planilla()
        elif opcion == 4:
            salirDelPrograma()
    except ValueError:
        print("Ingrese la opcion numerica correcta.")
