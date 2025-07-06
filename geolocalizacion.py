import requests

API_KEY = "ddcad19f-ecd4-4474-b674-d29b105ae67b"

def obtener_direccion(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {"q": ciudad, "locale": "es", "key": API_KEY}
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    if datos['hits']:
        lat = datos['hits'][0]['point']['lat']
        lon = datos['hits'][0]['point']['lng']
        return lat, lon
    else:
        print(f"No se encontró la ciudad: {ciudad}")
        return None, None

def calcular_ruta(origen, destino, modo):
    lat_o, lon_o = obtener_direccion(origen)
    lat_d, lon_d = obtener_direccion(destino)
    if None in [lat_o, lon_o, lat_d, lon_d]:
        return

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{lat_o},{lon_o}", f"{lat_d},{lon_d}"],
        "vehicle": modo,
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    if "paths" in datos:
        path = datos["paths"][0]
        distancia_km = path["distance"] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_min = path["time"] / 60000
        print(f"\n➡ Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"🕒 Duración estimada: {duracion_min:.2f} minutos")
        print("\n🧭 Narrativa del viaje:")
        for paso in path["instructions"]:
            print("-", paso["text"])
    else:
        print("No se pudo calcular la ruta.")

def main():
    while True:
        print("\n---- CALCULADORA DE DISTANCIAS ----")
        origen = input("Ciudad de origen (Chile): ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de destino (Argentina): ")
        if destino.lower() == 's':
            break

        print("Medios de transporte: car, foot, bike")
        modo = input("¿Qué medio de transporte desea usar? (escriba 'car', 'foot' o 'bike'): ").lower()
        if modo not in ['car', 'foot', 'bike']:
            print("Medio no válido. Se usará 'car' por defecto.")
            modo = 'car'

        calcular_ruta(origen, destino, modo)

        salir = input("\n¿Deseas salir? (presiona 's' para salir, cualquier otra tecla para continuar): ")
        if salir.lower() == 's':
            break

if __name__ == "__main__":
    main()
