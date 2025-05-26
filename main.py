from generator.generate_barcode import generar_codigo
from reader.read_barcode import leer_codigo


if __name__ == "__main__":
    # Generar codigo
    generar_codigo(nombre_archivo="producto123", datos="123456789012")
    # Leer codigo generado
    leer_codigo("barcodes/producto123.png")