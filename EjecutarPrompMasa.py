import requests
import json
import os
import time

# Función para cargar texto desde archivos
def cargar_texto(archivo):
    with open(archivo, 'r') as file:
        return file.read().strip()

# --- Contexto Base de datos ---
Contexto2023_1 = cargar_texto('Contextos/Datos2023-1.txt')
Contexto2023_2 = cargar_texto('Contextos/Datos2023-2.txt')

# --- Enunciados --- 
Ejercicio1_2023_1 = cargar_texto('Ejercicios/Ejercicio 1 2023-1.txt')
Ejercicio2_2023_1 = cargar_texto('Ejercicios/Ejercicio 2 2023-1.txt')
Ejercicio3_2023_1 = cargar_texto('Ejercicios/Ejercicio 3 2023-1.txt')
Ejercicio1_2023_2 = cargar_texto('Ejercicios/Ejercicio 1 2023-2.txt')
Ejercicio2_2023_2 = cargar_texto('Ejercicios/Ejercicio 2 2023-2.txt')

# --- Respuestas Correctas ---
RespuestaCorrecta_ejercicio_1_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 1 - 2023 -1 .txt')
RespuestaCorrecta_ejercicio_2_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 2 - 2023 -1 .txt')
RespuestaCorrecta_ejercicio_3_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 3 - 2023 -1 .txt')
RespuestaCorrecta_ejercicio_1_2023_2 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 1 - 2023 -2 .txt')
RespuestaCorrecta_ejercicio_2_2023_2 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 2 - 2023 -2 .txt')

# --- Prompts ---
PrompCorrectaIncorrecta = cargar_texto('Promp/RespuestaCorrectaIncorrecta.txt')
PrompIdentificarErroresLogicos = cargar_texto('Promp/IdentificaErroresLogicos.txt')
PrompIdentificaErroresSintaxis = cargar_texto('Promp/IdentificaErroresSintaxis.txt')
PrompElementosExtras = cargar_texto('Promp/IdentifcaElementosExtras.txt')
PrompProponersolucion = cargar_texto('Promp/ProponerSolucion.txt')
PrompCreaRespuesta = cargar_texto('Promp/RespuestaCreada.txt')
PrompExplicarEjercicio = cargar_texto('Promp/ExplicarEjercicio.txt')

# Función para enviar el prompt
def enviar_prompt(contexto, enunciado, respuesta, nombre_respuesta, modelo, prompt_template, version):
    prompt = prompt_template.format(
        contexto=contexto,
        enunciado=enunciado,
        respuesta=respuesta,
    )

    # Generar nombre de archivo automáticamente usando los nombres de las variables
    nombre_archivo = f"Respuesta_{nombre_respuesta}_{modelo}_{version}.txt"
    
    # Crear las carpetas para el modelo y versión si no existen
    carpeta_modelo = f"Modelo respuestas/{modelo}/{version}"

    # Crear las carpetas necesarias
    os.makedirs(carpeta_modelo, exist_ok=True)

    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_modelo, nombre_archivo)

    # Configuración de la solicitud
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": modelo,
        "prompt": prompt,
        "temperature": 0.7,
        "stream": False
    }
    
    # Iniciar el temporizador para medir el tiempo de respuesta
    start_time = time.time()
    print(f"Ejecutando prompt en {modelo}...")

    # Realizar la solicitud
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Calcular el tiempo de respuesta
    end_time = time.time()
    response_time = end_time - start_time  # Tiempo en segundos

    # Guardar en txt
    if response.status_code == 200:
        respuesta_llm = response.json().get('response', 'No se recibió una respuesta válida')
        tokens_recibidos = response.json().get('usage', {}).get('total_tokens', 'No disponible')
        tokens_enviados = len(prompt.split())  # Estimación simple de los tokens enviados (puede variar dependiendo del modelo)

        # Crear el contenido del archivo con las estadísticas de respuesta
        archivo_contenido = f"""
---------- Respuesta LLM: {modelo} ------------------
Respuesta generada:
{respuesta_llm}

---------- Estadísticas de Respuesta ------------------
Tiempo de respuesta: {response_time:.2f} segundos
Tokens enviados: {tokens_enviados}
Tokens recibidos: {tokens_recibidos}
"""
        # Escribir la respuesta y las estadísticas en el archivo
        with open(ruta_archivo, 'w') as file:
            file.write(archivo_contenido)

        print(f"Respuesta LLM guardada en '{ruta_archivo}'")
    else:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)

# Variables de entrada
modelos = ["llama3.1", "llama3.2"]
ejercicios = [
    (Contexto2023_1, Ejercicio1_2023_1, RespuestaCorrecta_ejercicio_1_2023_1, "2023_1_E1"),
    (Contexto2023_1, Ejercicio2_2023_1, RespuestaCorrecta_ejercicio_2_2023_1, "2023_1_E2"),
    (Contexto2023_1, Ejercicio3_2023_1, RespuestaCorrecta_ejercicio_3_2023_1, "2023_1_E3"),
    (Contexto2023_2, Ejercicio1_2023_2, RespuestaCorrecta_ejercicio_1_2023_2, "2023_2_E1"),
    (Contexto2023_2, Ejercicio2_2023_2, RespuestaCorrecta_ejercicio_2_2023_2, "2023_2_E2")
]

# Carpeta base
Carpeta = "1.Correctasv4"

# Bucle para ejecutar prompts
for modelo in modelos:
    for contexto, enunciado, respuesta, nombre_respuesta in ejercicios:
        enviar_prompt(contexto, enunciado, respuesta, nombre_respuesta, modelo, PrompCorrectaIncorrecta, Carpeta)
