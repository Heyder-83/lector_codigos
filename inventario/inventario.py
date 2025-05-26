import json
import os


DB_PATH = os.path.join("data", "productos.json")


def cargar_productos():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            f.write("[]")

    with open(DB_PATH, "r") as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)


def guardar_productos(productos):
    with open(DB_PATH, "w") as f:
        json.dump(productos, f, indent=4)


def agregar_producto(nombre: str, precio: float):
    productos = cargar_productos()
    nuevo_id = 1 if not productos else productos[-1]["id"] + 1

    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "codigo": f"{nuevo_id:012d}"  # código de 12 dígitos para código de barras
    }

    productos.append(producto)
    guardar_productos(productos)
    return producto
