import os
from generator.generate_barcode import generar_codigo
from reader.read_barcode import leer_codigo
from inventario.inventario import agregar_producto


if __name__ == "__main__":
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))

    producto = agregar_producto(nombre, precio)
    print(f"Producto registrado: {producto['nombre']} - ${producto['precio']}")

    nombre_archivo = str(producto['id'])
    generar_codigo(nombre_archivo=str(producto['id']), datos=str(producto['id']))

    codigo_barras = str(producto['id']).zfill(13)

    # Generar y leer el código de barras
    generar_codigo(nombre_archivo=codigo_barras, datos=codigo_barras)
    ruta = os.path.join("barcodes", f"{nombre_archivo}.png")
    leer_codigo(ruta)
