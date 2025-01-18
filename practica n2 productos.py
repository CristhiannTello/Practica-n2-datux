# PRACTICA NRO 2
# DEFINA EL SIGUIENTE DICCIONARIO

ventas = [
    {
        "fecha": "12-01-2023",
        "producto": "Producto_A",
        "cantidad": 50,
        "precio": 45.00,
        "promocion": True
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_AX",
        "cantidad": 160,
        "precio": 12.00,
        "promocion": False
    },
    {
        "fecha": "10-01-2023",
        "producto": "Producto_D",
        "cantidad": 20,
        "precio": 15.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_C",
        "cantidad": 10,
        "precio": 140.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_D",
        "cantidad": 1200,
        "precio": 1.00,
        "promocion": True
    }
]

# 1. CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
# 2. Mostrar el listado de ventas => puedes usar print(f"")
# 3. Añadir un producto
# 4. Calcular la suma total de las ventas
# 5. Calcular el promedio de ventas
# 6. Mostar el producto mas unidades vendidas
# 7. Mostrar el listado de productos


#Desarrollo de la práctica:

def mostrar_ventas():
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def anadir_producto():
    fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Está en promoción? (si/no): ").strip().lower() == "si"
    ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
    print("Producto agregado correctamente.")

def calcular_suma_total():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {total}")

def calcular_promedio_ventas():
    total_ventas = len(ventas)
    suma_total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"El promedio de ventas es: {promedio}")

def producto_mas_vendido():
    max_producto = max(ventas, key=lambda venta: venta['cantidad'])
    print(f"El producto con más unidades vendidas es: {max_producto['producto']} con {max_producto['cantidad']} unidades.")

def mostrar_productos():
    productos = set(venta['producto'] for venta in ventas)
    print("Listado de productos:")
    for producto in productos:
        print(f"- {producto}")

def menu():
    while True:
        print("\nMENU INTERACTIVO")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            anadir_producto()
        elif opcion == "3":
            calcular_suma_total()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_productos()
        elif opcion == "7":
            print("Gracias por su visita.")
            break
        else:
            print("Ingrese una opción valida, por favor.")

if __name__ == "__main__":
    menu()
