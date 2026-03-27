#Restricción: Todos los ejercicios deben resolverse con Python básico. No se permite el uso de librerías externas (NumPy, Pandas, etc.).
#Clean Code: Cada función debe tener docstring, nombres en snake_case, código legible y modular.

estudiantes = [
    {"nombre": "Ana","notas":[6.5, 7.0, 5.8]},
    {"nombre": "Luis","notas":[4.2, 5.1, 6.0]},
    {"nombre": "Sofía","notas":[3.9, 4.0, 4.5]},
    {"nombre": "Pedro","notas":[5.5, 6.1, 5.9]},
    {"nombre": "Valentina","notas":[7.0, 6.8, 6.9]},
    {"nombre": "Javier","notas":[4.0, 4.2, 4.1]},
    {"nombre": "Camila","notas":[5.0, 5.5, 5.8]},
    {"nombre": "Martín","notas":[3.5, 4.0, 4.2]},
    {"nombre": "Fernanda","notas":[6.2, 6.5, 6.0]},
    {"nombre": "Tomás","notas":[4.8, 5.0, 5.2]},
    {"nombre": "Josefa","notas":[5.9, 6.0, 6.1]},
    {"nombre": "Matías","notas":[3.8, 4.1, 4.0]},
    {"nombre": "Ignacio","notas":[6.7, 6.9, 7.0]},
    {"nombre": "Daniela","notas":[5.2, 5.4, 5.6]},
    {"nombre": "Sebastián","notas":[4.3, 4.5, 4.7]},
    {"nombre": "Gabriela","notas":[6.0, 6.2, 6.1]},
    {"nombre": "Felipe","notas":[5.7, 5.8, 5.9]},
    {"nombre": "Antonia","notas":[4.9, 5.0, 5.1]},
    {"nombre": "Vicente","notas":[3.7, 4.0, 4.3]},
    {"nombre": "Paula","notas":[6.3, 6.4, 6.5]},
]

texto = """
La ciencia de datos es un campo interdisciplinario que utiliza
métodos científicos y algoritmos para extraer conocimiento de
los datos. La estadística y la programación son herramientas
fundamentales para un científico de datos. Los datos pueden
ser estructurados o no estructurados. El análisis de datos
permite tomar decisiones basadas en evidencia.
"""
#3a)
def aplanar_notas(estudiantes):
    todas = []
    for estudiante in estudiantes:
        for nota in estudiante["notas"]:
            todas.append(nota)
            return todas

def contar_frecuencias(datos):
    frecuencias={}
    for valor in datos:
        if valor in frecuencias:
            frecuencias[valor]+=1
        else:
            frecuencias[valor]=1
    return frecuencias

def encontrar_moda(frecuencias):
    valor_moda=None
    cantidad_moda=0
    for valor,cantidad in frecuencias.items():
        if cantidad > cantidad_moda:
            cantidad_moda=cantidad
            valor_moda=valor
    return (valor_moda,cantidad_moda)

#3b)

def generar_histograma(frecuencias, ancho_max=25):
    freq_max = 0
    for cantidad in frecuencias.values():
        if cantidad > freq_max:
            freq_max = cantidad
    claves = list(frecuencias.keys())
    n = len(claves)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if claves[j] > claves[j + 1]:
                claves[j], claves[j + 1] = claves[j + 1], claves[j]
    print("\n  Histograma de notas")
    for clave in claves:
        cantidad = frecuencias[clave]
        bloques = round((cantidad / freq_max) * ancho_max)
        barra = "█" * bloques
        print(f"  {clave:.1f} | {barra:<25} ({cantidad})")

#3c)

def clasificar_en_tramos(datos, tramos):
    conteo = {}
    for nombre in tramos:
        conteo[nombre] = 0
    for valor in datos:
        for nombre, (minimo, maximo) in tramos.items():
            if minimo <= valor <= maximo:
                conteo[nombre] += 1
                break
    return conteo

#3d)

def limpiar_texto(texto):
    signos = '.,;:!?¡¿()[]{}"\'-'
    texto_limpio = texto.lower().replace("\n", " ")
    resultado = ""
    for caracter in texto_limpio:
        if caracter not in signos:
            resultado += caracter
    palabras = []
    for palabra in resultado.split(" "):
        if palabra != "":
            palabras.append(palabra)
    return " ".join(palabras)

def frecuencia_palabras(texto_limpio):
    palabras = texto_limpio.split(" ")
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def top_n_palabras(frecuencias, n=10):
    pares = list(frecuencias.items())
    largo = len(pares)
    for i in range(largo - 1):
        idx_max = i
        for j in range(i + 1, largo):
            if pares[j][1] > pares[idx_max][1]:
                idx_max = j
        pares[i], pares[idx_max] = pares[idx_max], pares[i]
    return pares[:n]


def diversidad_lexica(texto_limpio):
    palabras = texto_limpio.split(" ")
    total = 0
    unicas = {}
    for palabra in palabras:
        total += 1
        unicas[palabra] = True
    return len(unicas) / total

#3e)

def calcular_bigramas(texto_limpio):
    palabras = texto_limpio.split(" ")
    bigramas = {}
    for i in range(len(palabras) - 1):
        par = palabras[i] + " " + palabras[i + 1]
        if par in bigramas:
            bigramas[par] += 1
        else:
            bigramas[par] = 1
    return bigramas

#Menú prueba

if __name__ == "__main__":

    # 3a)
    print("=" * 50)
    print("  EJERCICIO 3a")
    print("=" * 50)
    todas_las_notas = aplanar_notas(estudiantes)
    print(f"  Total de notas aplanadas : {len(todas_las_notas)}")
    frecuencias_notas = contar_frecuencias(todas_las_notas)
    moda, cantidad_moda = encontrar_moda(frecuencias_notas)
    print(f"  Moda                     : {moda} (aparece {cantidad_moda} veces)")

    # 3b)
    print("=" * 50)
    print(" EJERCICIO 3b")
    print("=" * 50)
    generar_histograma(frecuencias_notas)

    # 3c)
    print("\n" + "=" * 50)
    print("  EJERCICIO 3c")
    print("=" * 50)
    tramos = {
        "Reprobado  (1.0 – 3.9)": (1.0, 3.9),
        "Suficiente (4.0 – 4.9)": (4.0, 4.9),
        "Aprobado   (5.0 – 5.9)": (5.0, 5.9),
        "Destacado  (6.0 – 7.0)": (6.0, 7.0),
    }
    conteo_tramos = clasificar_en_tramos(todas_las_notas, tramos)
    for tramo, cantidad in conteo_tramos.items():
        print(f"  {tramo} : {cantidad} notas")

    # 3d)
    print("\n" + "=" * 50)
    print("  EJERCICIO 3d — Análisis de texto")
    print("=" * 50)
    texto_limpio = limpiar_texto(texto)
    print(f"  Texto limpio (primeros 80 chars):")
    print(f"  {texto_limpio[:80]}")

    freq_palabras = frecuencia_palabras(texto_limpio)
    diversidad = diversidad_lexica(texto_limpio)
    print(f"\n  Diversidad léxica : {diversidad:.2%}")

    top10 = top_n_palabras(freq_palabras, n=10)
    print("\n  Top 10 palabras más frecuentes:")
    for palabra, freq in top10:
        print(f"  {palabra:<20} {freq}")

    # 3e)
    print("\n" + "=" * 50)
    print("  EJERCICIO 3e — Bigramas")
    print("=" * 50)
    bigramas = calcular_bigramas(texto_limpio)
    top_bigramas = top_n_palabras(bigramas, n=5)
    print("  Top 5 bigramas más frecuentes:")
    for bigrama, freq in top_bigramas:
        print(f"  {bigrama:<25} {freq}")