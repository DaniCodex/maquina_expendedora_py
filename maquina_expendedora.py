import time
import random
import os
from productos_maquina import maquina
from cantidad_billetes import monedas  


"""ADMINISTRAR BASE DE DATOS (CODIGO)"""
def menuPrincipal():
    while True:
        limpiarTerminal()
        print("+----------------------------------------------------+")
        print("|              🎰 ALFREDITO'S MACHINE                |")
        print("|----------------------------------------------------|")
        print("| 1) Usar máquina expendedora                        |")
        print("| 2) Administrar base de datos                       |")
        print("| 3) Salir                                           |")
        print("+----------------------------------------------------+")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            interfazMaquina()
            divisaPago()
        elif opcion == "2":
            administrarBD()
        elif opcion == "3":
            print("Gracias por usar ALFREDITO'S MACHINE")
            break
        else:
            print("Opción no válida, intente de nuevo.")
            time.sleep(2)

def administrarBD():
    while True:
        limpiarTerminal()
        print("+----------------------------------------------------+")
        print("|              🛠 ADMINISTRAR BASE DE DATOS           |")
        print("|----------------------------------------------------|")
        print("| 1) Ver productos                                   |")
        print("| 2) Modificar precio de producto                    |")
        print("| 3) Modificar cantidad de producto                  |")
        print("| 4) Agregar nuevo producto                          |")
        print("| 5) Eliminar producto                               |")
        print("| 6) Ver dinero                                      |")
        print("| 7) Administrar dinero                              |")
        print("| 8) Volver al menú principal                        |")
        print("+----------------------------------------------------+")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            verProductos()
        elif opcion == "2":
            modificarPrecio()
        elif opcion == "3":
            modificarCantidad()
        elif opcion == "4":
            agregarProducto()
        elif opcion == "5":
            eliminarProducto()
        elif opcion == "6":
            verDinero()
        elif opcion == "7":
            administrarDinero()
        elif opcion == "8":
            break
        else:
            print("Opción no válida, intente de nuevo.")
            time.sleep(2)

def verProductos():
    limpiarTerminal()
    print("+----------------------------------------------------+")
    print("|                   📦 PRODUCTOS                     |")
    print("+----------------------------------------------------+")
    for key, value in maquina.items():
        print(key)
        print(f"ID: {key} | Nombre: {value['nombre']} | Precio: {value['precio']} | Cantidad: {value['cantidad']}")
    input("\nPresione Enter para continuar...")

def verDinero():
    limpiarTerminal()
    print("+----------------------------------------------------+")
    print("|              💵 ADMINISTRAR DINERO                 |")
    print("|----------------------------------------------------|")
    print(f"|{monedas[1]['tipo']}-->{monedas[1]['cantidad']}   {monedas[2]['tipo']}-->{monedas[2]['cantidad']}           |")
    print(f"|{monedas[3]['tipo']}-->{monedas[3]['cantidad']}   {monedas[4]['tipo']}-->{monedas[4]['cantidad']}           |")
    print(f"|{monedas[5]['tipo']}--> {monedas[5]['cantidad']}   {monedas[6]['tipo']}-->{monedas[6]['cantidad']}          |")
    print(f"|{monedas[7]['tipo']}--> {monedas[7]['cantidad']}   {monedas[8]['tipo']}-->{monedas[8]['cantidad']}          |")
    print(f"|{monedas[9]['tipo']}--> {monedas[9]['cantidad']}   {monedas[10]['tipo']}-->{monedas[10]['cantidad']}        |")
    input("\nPresione Enter para continuar...")

def modificarPrecio():
    limpiarTerminal()
    verProductos()
    IDProducto = int(input("Ingrese el ID del producto a modificar: "))
    if IDProducto in maquina:
        nuevoPrecio = float(input("Ingrese el nuevo precio: "))
        maquina[IDProducto]['precio'] = nuevoPrecio
        print("Precio modificado con éxito.")
    else:
        print("ID de producto no encontrado.")
    time.sleep(2)

def modificarCantidad():
    limpiarTerminal()
    verProductos()
    IDProducto = int(input("Ingrese el ID del producto a modificar: "))
    if IDProducto in maquina:
        nuevaCantidad = int(input("Ingrese la nueva cantidad: "))
        maquina[IDProducto]['cantidad'] = nuevaCantidad
        print("Cantidad modificada con éxito.")
    else:
        print("ID de producto no encontrado.")
    time.sleep(2)

def agregarProducto():
    limpiarTerminal()
    verProductos()
    IDProducto = int(input("Ingrese el nuevo ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    maquina[IDProducto] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    print("Producto agregado con éxito.")
    time.sleep(2)

def eliminarProducto():
    limpiarTerminal()
    verProductos()
    IDProducto = int(input("Ingrese el ID del producto a eliminar: "))
    if IDProducto in maquina:
        del maquina[IDProducto]
        print("Producto eliminado con éxito.")
    else:
        print("ID de producto no encontrado.")
    time.sleep(2)

def administrarDinero():
    limpiarTerminal()
    verDinero()

    idDinero = int(input("Ingrese el ID del precio a modificar: "))
    if idDinero in maquina:
        nuevaCantidad = int(input("Ingrese la nueva cantidad: "))
        monedas[idDinero]['cantidad'] = nuevaCantidad
        print("Dinero modificada con éxito.")
    else:
        print("ID de producto no encontrado.")
    time.sleep(2)


"""CODIGO FRONTEND"""

def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def comprobarDinero(dinero):
    if dinero in [0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100]:
        return True
    else:
        print("-----------------------------------------------------")
        print("🚫 POR FAVOR INGRESE UN MONTO  REAL")
        print("-----------------------------------------------------")
        return False

def sumarDineroDB(montoIngresado):
     for i in range(1, 11):
        if montoIngresado == monedas[i]['tipo']:
            monedas[i]['cantidad'] += 1
            break

def interfazMaquina():
    global divisa, dineroIngresado, id
    limpiarTerminal()

    print("+----------------------------------------------------+")
    print("|              🎰 ALFREDITO'S MACHINE                |")
    print("|----------------------------------------------------|")
    print("| ID    NOMBRE            PRECIO         CANTIDAD    |")
    print("|----------------------------------------------------|")
    print(f"| 1     {maquina[1]['nombre']}          {maquina[1]['precio']}               {maquina[1]['cantidad']}        |")
    print(f"| 2     {maquina[2]['nombre']}          {maquina[2]['precio']}             {maquina[2]['cantidad']}        |")
    print(f"| 3     {maquina[3]['nombre']}              {maquina[3]['precio']}               {maquina[3]['cantidad']}        |")
    print(f"| 4     {maquina[4]['nombre']}            {maquina[4]['precio']}             {maquina[4]['cantidad']}        |")
    print(f"| 5     {maquina[5]['nombre']}           {maquina[5]['precio']}             {maquina[5]['cantidad']}        |")
    print(f"| 6     {maquina[6]['nombre']}     {maquina[6]['precio']}             {maquina[6]['cantidad']}        |")
    print(f"| 7     {maquina[7]['nombre']}      {maquina[7]['precio']}              {maquina[7]['cantidad']}        |")
    print(f"| 8     {maquina[8]['nombre']}       {maquina[8]['precio']}             {maquina[8]['cantidad']}        |")
    print("+----------------------------------------------------+")
    print()
    print("-----------------------------------------------------")
    print("👉 ¿Como desea pagar el producto?")
    print("-----------------------------------------------------")
    print("1) SOLES")
    print("2) DOLARES")
    print("3) EUROS")
    print("-----------------------------------------------------")
    
    divisa = input("👉 SELECCIONE UNA OPCIÓN (1,2 o 3): ")

    if divisa == "alfredito1234":
        menuPrincipal()
        return

    dineroIngresado = float(input("💸 INGRESE SU DINERO: "))

    sumarDineroDB(dineroIngresado)

    while (not comprobarDinero(dineroIngresado)):
        dineroIngresado = float(input("💸 INGRESE SU DINERO: "))

    id = int(input("🍾 SELECCIONE SU PRODUCTO: "))

    print("")
    
interfazMaquina()


def restarDineroDB(monto, cantidad):
    for i in range(1, 11):
        if monto == monedas[i]['tipo']:
            monedas[i]['cantidad'] -= cantidad
            break

def devolverProducto(pagoTotal, vueltoTotal):
    pagoTotal = round(pagoTotal, 2)
    vueltoTotal = round(vueltoTotal, 2)

    bd_dinero = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10]
    
    vuelto = vueltoTotal  
    vueltoEfectivo = []
    for monto in bd_dinero:
        cantidad = int(vuelto // monto)
        if cantidad > 0:
            if monto in [100, 50, 20, 10]:
                vueltoEfectivo.append(f"{cantidad} billete(s) de {monto} soles")
            elif monto in [0.50,0.20,0.10]:
                vueltoEfectivo.append(f"{cantidad} moneda(s) de {monto} centimos")
            else:
                vueltoEfectivo.append(f"{cantidad} moneda(s) de {monto} soles")
            vuelto = round(vuelto - cantidad * monto,2)
            restarDineroDB(monto, cantidad)
    
    print("⏳ Procesando....")
    time.sleep(random.randint(1, 5))
    print("🖨️ Imprimiendo boleta...")
    time.sleep(random.randint(1, 5))
    limpiarTerminal()
    print("")
    print("+----------------------------")
    print("| 🙏 ¡GRACIAS POR SU COMPRA!")
    print("+----------------------------")
    print(f"|👉 Producto: {maquina[id]['nombre']}         ")
    print(f"|👉 Precio Producto: S/ {maquina[id]['precio']}   ")
    print(f"|👉 Pago Ingresado: S/ {pagoTotal}  ")
    print(f"|👉 Vuelto Total: S/ {vueltoTotal}    ")
    print("")
    print("+----------------------------")
    print("|💵 VUELTO EN EFECTIVO:        ")
    print("+----------------------------")
    for moneda in vueltoEfectivo:
        print(f"|👉  {moneda}    ")
    print("")
    input("\nPresione Enter para continuar...")
    interfazMaquina()
    divisaPago()

def solicitarDineroAdicional():
    dineroSuma = dineroIngresado
    montoAlcanzado = False

    while not montoAlcanzado:
        dineroFaltante = float(input("Ingrese lo restante: "))

        while not comprobarDinero(dineroFaltante):
            dineroFaltante = float(input("Ingrese un monto válido: "))
        else:
            dineroSuma += dineroFaltante
            if dineroSuma == maquina[id]["precio"]:
                vuelto = 0
                maquina[id]['cantidad'] -= 1
                devolverProducto(dineroSuma, vuelto)
                montoAlcanzado = True
            elif dineroSuma > maquina[id]["precio"]:
                vuelto = dineroSuma - maquina[id]["precio"]
                maquina[id]['cantidad'] -= 1
                devolverProducto(dineroSuma, vuelto)
                montoAlcanzado = True
            else:
                print(f"Dinero insuficiente. Necesita {maquina[id]['precio'] - dineroSuma} más.")

def manejarDineroInsuficiente():
    print("+---------------------+")
    print("| Dinero insuficiente |")
    print("+---------------------+")
    print("| 1.- ✅ SI           |")
    print("| 2.- ❌ NO           |")
    print("+---------------------+")
    print("")
    dineroExtra = input("¿DESEA COMPLETAR EL MONTO?: ")
    print("----------------------------")

    if dineroExtra == "1":
        solicitarDineroAdicional()
    else: 
        print("-----------------------------------------------------")
        print("Recoga su dinero de la máquina")
        print("")

def procesarPago(montoIngresado):
    if montoIngresado > maquina[id]['precio']:
        vuelto = montoIngresado - maquina[id]['precio']
        maquina[id]['cantidad'] -= 1
        devolverProducto(montoIngresado, vuelto)
    elif montoIngresado == maquina[id]['precio']:
        vuelto = maquina[id]["precio"] - montoIngresado
        maquina[id]['cantidad'] -= 1
        devolverProducto(montoIngresado, vuelto)
    else:
        manejarDineroInsuficiente()

def divisaPago():
    if divisa == "1":
        procesarPago(dineroIngresado)
    elif divisa == "2":
        dolarConvertido = dineroIngresado * 3.71
        procesarPago(dolarConvertido)
    elif divisa == "3":
        euroConvertido = dineroIngresado * 4.08
        procesarPago(euroConvertido)
    elif divisa == "alfredito1234":
        return
    else:
        print("Por ahora solo tenemos estas 3 divisas!!!")
        time.sleep(3)
        interfazMaquina()
        divisaPago()
divisaPago()
