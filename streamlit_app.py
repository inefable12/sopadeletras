import streamlit as st
import random
import numpy as np

# Función para generar una sopa de letras
def generar_sopa_de_letras(palabras, tamaño=10):
    sopa = np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), (tamaño, tamaño))
    for palabra in palabras:
        palabra = palabra.upper()
        colocada = False
        intentos = 0
        while not colocada and intentos < 100:
            direccion = random.choice(['H', 'V', 'D'])
            if direccion == 'H':
                fila = random.randint(0, tamaño - 1)
                col = random.randint(0, tamaño - len(palabra))
                if all([sopa[fila, col+i] in ('', palabra[i]) for i in range(len(palabra))]):
                    for i in range(len(palabra)):
                        sopa[fila, col+i] = palabra[i]
                    colocada = True
            elif direccion == 'V':
                fila = random.randint(0, tamaño - len(palabra))
                col = random.randint(0, tamaño - 1)
                if all([sopa[fila+i, col] in ('', palabra[i]) for i in range(len(palabra))]):
                    for i in range(len(palabra)):
                        sopa[fila+i, col] = palabra[i]
                    colocada = True
            elif direccion == 'D':
                fila = random.randint(0, tamaño - len(palabra))
                col = random.randint(0, tamaño - len(palabra))
                if all([sopa[fila+i, col+i] in ('', palabra[i]) for i in range(len(palabra))]):
                    for i in range(len(palabra)):
                        sopa[fila+i, col+i] = palabra[i]
                    colocada = True
            intentos += 1
    return sopa

# Función principal de la app
def main():
    st.title("Generador de Sopa de Letras")
    
    # Botón para cargar archivo
    archivo = st.file_uploader("Cargar archivo de texto", type=["txt"])
    
    if archivo is not None:
        palabras = archivo.read().decode("utf-8").splitlines()
        palabras = [palabra.strip() for palabra in palabras if palabra.strip()]
        
        # Mostrar palabras
        st.write("Palabras para buscar en la sopa:")
        st.write(", ".join(palabras))
        
        # Generar la sopa de letras
        tamaño = max(len(max(palabras, key=len)), 10)  # Ajustar tamaño
        sopa = generar_sopa_de_letras(palabras, tamaño=tamaño)
        
        # Mostrar la sopa de letras
        st.write("Sopa de letras:")
        st.write('\n'.join([' '.join(fila) for fila in sopa]))

        # Aquí puedes implementar una interfaz interactiva con PyDeck o algún módulo adicional si deseas que el usuario marque palabras

        # Cuando el usuario termina, mostrar globos
        if st.button("He terminado la sopa"):
            st.balloons()

# Ejecutar la app
if __name__ == "__main__":
    main()
