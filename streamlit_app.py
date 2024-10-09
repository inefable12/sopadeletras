import streamlit as st
import numpy as np
import random

# Definir una función para generar la sopa de letras
def generar_sopa(palabras, tamaño=10):
    sopa = np.full((tamaño, tamaño), '.', dtype=str)
    direcciones = [(0,1), (1,0), (1,1), (-1,1)]
    
    for palabra in palabras:
        colocada = False
        while not colocada:
            fila = random.randint(0, tamaño-1)
            col = random.randint(0, tamaño-1)
            direccion = random.choice(direcciones)
            if puede_colocar(palabra, sopa, fila, col, direccion):
                colocar_palabra(palabra, sopa, fila, col, direccion)
                colocada = True
    
    # Completar con letras aleatorias
    for i in range(tamaño):
        for j in range(tamaño):
            if sopa[i][j] == '.':
                sopa[i][j] = chr(random.randint(65, 90))  # Letras mayúsculas aleatorias

    return sopa

# Verificar si se puede colocar la palabra en la posición
def puede_colocar(palabra, sopa, fila, col, direccion):
    for i in range(len(palabra)):
        nueva_fila = fila + i * direccion[0]
        nueva_col = col + i * direccion[1]
        if nueva_fila < 0 or nueva_fila >= sopa.shape[0] or nueva_col < 0 or nueva_col >= sopa.shape[1]:
            return False
        if sopa[nueva_fila][nueva_col] != '.' and sopa[nueva_fila][nueva_col] != palabra[i]:
            return False
    return True

# Colocar la palabra en la sopa
def colocar_palabra(palabra, sopa, fila, col, direccion):
    for i in range(len(palabra)):
        nueva_fila = fila + i * direccion[0]
        nueva_col = col + i * direccion[1]
        sopa[nueva_fila][nueva_col] = palabra[i]

# Definir la interfaz de Streamlit
st.title("Sopa de Letras Interactiva")
st.write("Encuentra las siguientes palabras:")

# Definir las palabras a buscar
palabras = ["PYTHON", "STREAMLIT", "CODIGO", "GITHUB", "IA"]

# Mostrar las palabras
for palabra in palabras:
    st.write(f"- {palabra}")

# Generar la sopa de letras
sopa = generar_sopa(palabras)

# Mostrar la sopa de letras
for fila in sopa:
    st.write(" ".join(fila))

# Almacenar palabras encontradas por el usuario
palabras_encontradas = st.multiselect("Selecciona las palabras encontradas:", palabras)

# Puntaje
puntaje = len(palabras_encontradas)
st.write(f"Puntaje: {puntaje}/{len(palabras)}")

# Mostrar globos si todas las palabras son encontradas
if puntaje == len(palabras):
    st.balloons()
    st.write("¡Felicidades! Has encontrado todas las palabras.")
