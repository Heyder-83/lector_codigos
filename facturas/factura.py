import os
from datetime import datetime

def generar_factura(productos_seleccionados, carpeta='facturas_guardadas'):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum([producto['precio'] for producto in productos_seleccionados])

    contenido = f"FACTURA - {fecha}"
    contenido += "-" * 40 + "\n"
    for p in productos_seleccionados:
        contenido += f"{p['nombre']} - ${p['precio']}\n"
    contenido += "-" * 40 + "\n"
    contenido += f"TOTAL: ${total}\n"

    nombre_archivo = f"factura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, "w", encoding='utf-8') as f:
        f.write(contenido)

    
    print(f"Factura generada: {ruta}")