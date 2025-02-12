from io import open

class cliente:
    nombre = " "
    cantidad_p = 0
    cantidad_b = 0
    tarjeta = " "
    total = 0

    def __init__(self, nombre, cantidad_p, cantidad_b, tarjeta, total):
        self.nombre = nombre
        self.cantidad_p = cantidad_p   
        self.cantidad_b = cantidad_b
        self.tarjeta = tarjeta
        self.total = total

    def SetTotal(self, total):    
        self.total = total

    def calculo_B(self, cantidad_b, cantidad_p):
        cant_Max = cantidad_p * 7
        if cantidad_b > cant_Max:
            return False
        else:
            return True

    def calculoD1(self, obj):
        if obj.cantidad_b > 5:
            descuento = obj.total * 0.15
            obj.SetTotal(obj.total - descuento)
            return True
        return False

    def calculoD2(self, obj):
        if obj.cantidad_b in [3, 4, 5]:
            descuento = obj.total * 0.1
            obj.SetTotal(obj.total - descuento)
            return True
        return False

    def calculoD3(self, obj):
        if obj.tarjeta.lower() == "si":
            descuento = obj.total * 0.10
            obj.SetTotal(obj.total - descuento)
            return True
        return False                                            

def main():
    opc = 0
    compras = []  # Lista para almacenar las compras
    suma_totales = 0  # Variable para acumular la suma de los totales

    while opc != 3:
        print("\n" + "Bienvenido a la compra de boletos de CINECO" )
        print('-'*50)
        print("1. Comprar boletos")
        print("2. Ver boletos comprados")
        print("3. Salir" +"\n")
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            nombre = input("Ingrese su nombre: ")
            cantidad_p = int(input("Ingrese la cantidad de personas: "))
            cantidad_b = int(input("Ingrese la cantidad de boletos: "))
            total = cantidad_b * 12

            tarjeta = input("¿Usará tarjeta Cineco? si/no: ")

            obj = cliente(nombre, cantidad_p, cantidad_b, tarjeta, total)

            if not obj.calculo_B(cantidad_b, cantidad_p):
                print("La cantidad de boletos no puede ser mayor a 7 por persona")
                print("por favor agregue personas o quite boletos"+"\n")
                print('-'*50)
                print("1. Cantidad de personas")
                print("2. Cantidad de boletos")
                op2 = input("¿Qué desea cambiar?: ")

                if op2 == "1":
                    cantidad_p = int(input("Ingrese la cantidad de personas: "))
                    total = cantidad_b * 12
                elif op2 == "2":
                    cantidad_b = int(input("Ingrese la cantidad de boletos: "))
                    total = cantidad_b * 12
                else:
                    continue  # Salta el resto y vuelve a pedir opciones

            obj.calculoD2(obj)
            obj.calculoD1(obj)
            obj.calculoD3(obj)

            print("-"*50)
            print("Gracias por tu compra " + obj.nombre)
            print("Tu total a pagar es de: ${:.2f}".format(obj.total))
            print("-"*50)

            # Guardar la compra en la lista y acumular el total
            compras.append({'Nombre': obj.nombre, 'Total': obj.total})
            suma_totales += obj.total  # Acumular el total

        if opc == 2:
            for compra in compras:
                print(compra)
            continue 

        if opc == 3:
            # Escribir todas las compras en el archivo
            with open('ventas.txt', 'w') as fichero:
                for compra in compras:
                    texto = "Nombre: " + compra['Nombre'] + "\n" + "Vendido: " + str(compra['Total']) + "\n"
                    fichero.write(texto)
                # Escribir la suma de los totales
                fichero.write("\nTotal de ventas: ${:.2f}".format(suma_totales))
            print("\n" + "Gracias por su compra")

if __name__ == "__main__":
    main()