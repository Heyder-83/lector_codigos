import barcode
from barcode.writer import ImageWriter
import os


def generar_codigo(nombre_archivo: str, datos: str, carpeta: str = "barcodes"):
    """Genera un codigo de barras tipo Code128 y lo guarda como imagen PNG"""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    code_class = barcode.get_barcode_class('code128')
    codigo = code_class(datos, writer=ImageWriter())

    ruta_completa = os.path.join(carpeta, f"{nombre_archivo}.png")
    codigo.save(ruta_completa)

    print(f"Código generado: {ruta_completa}")
