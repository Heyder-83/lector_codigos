from reader.scan_input import escanear_codigo, buscar_producto
from facturas.factura import generar_factura

def flujo_venta():
    productos_seleccionados = []

    while True:
        print("\nEscanea un producto o presiona ENTER para finalizar la compra.")
        codigo = input("Código de barras: ").strip()

        if not codigo:
            break

        producto = buscar_producto(codigo)
        if producto:
            productos_seleccionados.append(producto)
            print(f"✅ Agregado: {producto['nombre']} - ${producto['precio']}")
        else:
            print("Producto no registrado.")
            respuesta = input("¿Deseas registrarlo? (s/n): ").lower()
            if respuesta == "s":
                escanear_codigo()  # permite registrarlo
            else:
                print("Producto ignorado.")

    if productos_seleccionados:
        generar_factura(productos_seleccionados)
    else:
        print("\nNo se escanearon productos. No se generó factura.")


if __name__ == "__main__":
    flujo_venta()
