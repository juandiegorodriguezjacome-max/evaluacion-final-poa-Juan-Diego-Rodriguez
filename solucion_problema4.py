def contar_titulos_filtrados(matriz_videoteca, umbral_calificacion, anio_limite):
    contador = 0  # Aquí guardaremos cuántas películas cumplen
    
    # Recorremos la matriz fila por fila usando un ciclo for
    for pelicula in matriz_videoteca:
        # Separamos los datos de la película actual según su posición en la lista
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        
        # Lógica de negocio: ¿Es popular (Calificación >= umbral) Y reciente (Año >= límite)?
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1  # Si cumple ambas, sumamos 1 al contador
            print(f" -> Cumple: {titulo} ({anio}) - Calif: {calificacion}")
            
    return contador  # Al final, devolvemos el total acumulado
def main():# (Aquí va la matriz del Paso 2...)
    videoteca = [
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Parasite", 2019, 8.5, "Drama/Suspenso"],
        ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
        ["Everything Everywhere All at Once", 2022, 8.0, "Acción/Sci-Fi"],
        ["Oppenheimer", 2023, 8.9, "Biografía/Drama"],
        ["Dune: Part Two", 2024, 8.8, "Ciencia Ficción"],
        ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
        ["Inception", 2010, 8.8, "Acción/Sci-Fi"]
    ]
    
    print("=== FILTRADO DE VIDEOTECA DIGITAL ===")
    
    # Pedimos los datos al usuario
    umbral_c = float(input("Ingrese la calificación mínima (1 al 10): "))
    anio_l = int(input("Ingrese el año límite (ej. 2020): "))
    
    print("\nBuscando películas...")
    
    # Llamamos a la función de arriba pasándole los datos
    total_cumplen = contar_titulos_filtrados(videoteca, umbral_c, anio_l)
    
    # Mostramos el conteo final exigido por la guía
    print(f"\nTotal de títulos que cumplen con ambos criterios: {total_cumplen}")
    print("=====================================")

# Esta línea final le dice a Python que ejecute la función main() al abrir el archivo
if __name__ == "__main__":
    main()# MÓDULO DE LÓGICA DE NEGOCIO
def contar_titulos_filtrados(matriz_videoteca, umbral_calificacion, anio_limite):
    contador = 0
    for pelicula in matriz_videoteca:
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
            print(f" -> Cumple: {titulo} ({anio}) - Calif: {calificacion}")
            
    return contador

# PROGRAMA PRINCIPAL
def main():
    videoteca = [
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Parasite", 2019, 8.5, "Drama/Suspenso"],
        ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
        ["Everything Everywhere All at Once", 2022, 8.0, "Acción/Sci-Fi"],
        ["Oppenheimer", 2023, 8.9, "Biografía/Drama"],
        ["Dune: Part Two", 2024, 8.8, "Ciencia Ficción"],
        ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
        ["Inception", 2010, 8.8, "Acción/Sci-Fi"]
    ]
    
    print("=== FILTRADO DE VIDEOTECA DIGITAL ===")
    umbral_c = float(input("Ingrese la calificación mínima (1 al 10): "))
    anio_l = int(input("Ingrese el año límite (ej. 2015): "))
    
    print("\nBuscando películas...")
    total_cumplen = contar_titulos_filtrados(videoteca, umbral_c, anio_l)
    
    print(f"\nTotal de títulos que cumplen con ambos criterios: {total_cumplen}")
    print("=====================================")

if __name__ == "__main__":
    main()
    
    # Creamos la matriz con 8 películas (el formato es: [Título, Año, Calificación, Género])
    videoteca = [
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Parasite", 2019, 8.5, "Drama/Suspenso"],
        ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
        ["Everything Everywhere All at Once", 2022, 8.0, "Acción/Sci-Fi"],
        ["Oppenheimer", 2023, 8.9, "Biografía/Drama"],
        ["Dune: Part Two", 2024, 8.8, "Ciencia Ficción"],
        ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
        ["Inception", 2010, 8.8, "Acción/Sci-Fi"]
    ]
