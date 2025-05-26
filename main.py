import os


from generator.generate_barcode import generar_codigo
from reader.read_barcode import leer_codigo


if __name__ == "__main__":
    nombre_archivo = "producto123"
    datos = "123456789012"
    # Generar codigo
    generar_codigo(nombre_archivo="producto123", datos="123456789012")
    # Leer codigo generado
    ruta = os.path.join("barcodes", f"{nombre_archivo}.png")
    leer_codigo(ruta)
