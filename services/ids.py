from datetime import datetime


def generar_id(prefijo):
    fecha = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefijo}-{fecha}"
