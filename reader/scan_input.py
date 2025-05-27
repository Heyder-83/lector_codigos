import json
from inventario.inventario import cargar_productos, guardar_productos, agregar_producto
from generator.generate_barcode import generar_codigo
from facturas.factura import generar_factura


def buscar_producto(codigo):
    productos = cargar_productos()
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def escanear_codigo():
    print("Escanea el producto (presiona ENTER para finalizar): \n")
    carrito = []

    while True:
        codigo = input("Codigo de barras: ").strip()
        if codigo == "":
            break

        codigo = codigo.zfill(13)

        producto = buscar_producto(codigo)

        if producto:
            print(f"Producto registrado: {producto['nombre']} - ${producto['precio']}")
            carrito.append(producto)
        else:
            print("Producto no registrado")
            respuesta = input("¿Desea registrar el producto? (s/n): ").lower()
            if respuesta == "s":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                nuevo_producto = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio
                }
                productos = cargar_productos()
                productos.append(nuevo_producto)
                guardar_productos(productos)
                generar_codigo(nombre_archivo=codigo, datos=codigo)
                print(f"Producto registrado: {nombre} - ${precio}")
                carrito.append(nuevo_producto)
            else:
                print("producto no registrado")
    if carrito:
        print("\n Resumen de compra:")
        total = 0
        for p in carrito:
            print(f" - {p['nombre']} - ${p['precio']}")
            total += float(p['precio'])
        print(f"\n Total a pagar: ${total:.2f}")
        generar_factura(carrito)
    else:
        print("No se escaneo ningun producto")
