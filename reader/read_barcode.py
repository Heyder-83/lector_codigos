from pyzbar.pyzbar import decode
from PIL import Image


def leer_codigo(ruta_imagen: str):
    """Lee y decodifica un codigo de barras desde una imagen PNG o JPG"""
    try:
        imagen = Image.open(ruta_imagen)
        codigos = decode(imagen)

        if not codigos:
            print("No se detectaron códigos.")
            return

        for codigo in codigos:
            print(f"Tipo: {codigo.type}, Datos: {codigo.data.decode('utf-8')}")
    except FileNotFoundError:
        print(f"Imagen no encontrada: {ruta_imagen}")