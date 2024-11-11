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

# --- Respuestas de casos de prueba ---

# Respuestas correctas
RespuestaCorrecta_ejercicio_1_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 1 - 2023 -1 .txt')
RespuestaCorrecta_ejercicio_2_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 2 - 2023 -1 .txt')
RespuestaCorrecta_ejercicio_3_2023_1 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 3 - 2023 -1 .txt')

RespuestaCorrecta_ejercicio_1_2023_2 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 1 - 2023 -2 .txt')
RespuestaCorrecta_ejercicio_2_2023_2 = cargar_texto('Respuestas/Respuestas Correctas/Ejercicio 2 - 2023 -2 .txt')

# Respuestas incorrectas
RespuestaIncorrecta_ejercicio_1_2023_1 = cargar_texto('Respuestas/Respuestas incorrectas/Ejercicio 1 - 2023 -1 .txt')
RespuestaIncorrecta_ejercicio_2_2023_1 = cargar_texto('Respuestas/Respuestas incorrectas/Ejercicio 2 - 2023 -1 .txt')
RespuestaIncorrecta_ejercicio_3_2023_1 = cargar_texto('Respuestas/Respuestas incorrectas/Ejercicio 3 - 2023 -1 .txt')

RespuestaIncorrecta_ejercicio_1_2023_2 = cargar_texto('Respuestas/Respuestas incorrectas/Ejercicio 1 - 2023 -2 .txt')
RespuestaIncorrecta_ejercicio_2_2023_2 = cargar_texto('Respuestas/Respuestas incorrectas/Ejercicio 2 - 2023 -2 .txt')

# Respuesta Error Logicos
RespuestaErrorLogico_ejercicio_1_2023_1 = cargar_texto('Respuestas/Error logico/Ejercicio 1 - 2023 -1 .txt')
RespuestaErrorLogico_ejercicio_2_2023_1 = cargar_texto('Respuestas/Error logico/Ejercicio 2 - 2023 -1 .txt')
RespuestaErrorLogico_ejercicio_3_2023_1 = cargar_texto('Respuestas/Error logico/Ejercicio 3 - 2023 -1 .txt')

RespuestaErrorLogico_ejercicio_1_2023_2 = cargar_texto('Respuestas/Error logico/Ejercicio 1 - 2023 -2 .txt')
RespuestaErrorLogico_ejercicio_2_2023_2 = cargar_texto('Respuestas/Error logico/Ejercicio 2 - 2023 -2 .txt')

# Respuesta Error de sintaxis
RespuestaErrorSintaxis_ejercicio_1_2023_1 = cargar_texto('Respuestas/Error sintaxis/Ejercicio 1 - 2023 -1 .txt')
RespuestaErrorSintaxis_ejercicio_2_2023_1 = cargar_texto('Respuestas/Error sintaxis/Ejercicio 2 - 2023 -1 .txt')
RespuestaErrorSintaxis_ejercicio_3_2023_1 = cargar_texto('Respuestas/Error sintaxis/Ejercicio 3 - 2023 -1 .txt')

RespuestaErrorSintaxis_ejercicio_1_2023_2 = cargar_texto('Respuestas/Error sintaxis/Ejercicio 1 - 2023 -2 .txt')
RespuestaErrorSintaxis_ejercicio_2_2023_2 = cargar_texto('Respuestas/Error sintaxis/Ejercicio 2 - 2023 -2 .txt')

# Respuesta elementos extas
RespuestaElementosExtras_ejercicio_1_2023_1 = cargar_texto('Respuestas/Error Elementos extras/Ejercicio 1 - 2023 -1 .txt')
RespuestaElementosExtras_ejercicio_2_2023_1 = cargar_texto('Respuestas/Error Elementos extras/Ejercicio 2 - 2023 -1 .txt')
RespuestaElementosExtras_ejercicio_3_2023_1 = cargar_texto('Respuestas/Error Elementos extras/Ejercicio 3 - 2023 -1 .txt')

RespuestaElementosExtras_ejercicio_1_2023_2 = cargar_texto('Respuestas/Error Elementos extras/Ejercicio 1 - 2023 -2 .txt')
RespuestaElementosExtras_ejercicio_2_2023_2 = cargar_texto('Respuestas/Error Elementos extras/Ejercicio 2 - 2023 -2 .txt')

# Proponer Respuesta Con respuesta
RespuestaPropuesta_ejercicio_1_2023_1 = cargar_texto('Respuestas/Sugerir respuesta/Ejercicio 1 - 2023 -1 .txt')
RespuestaPropuesta_ejercicio_2_2023_1 = cargar_texto('Respuestas/Sugerir respuesta/Ejercicio 2 - 2023 -1 .txt')
RespuestaPropuesta_ejercicio_3_2023_1 = cargar_texto('Respuestas/Sugerir respuesta/Ejercicio 3 - 2023 -1 .txt')

RespuestaPropuesta_ejercicio_1_2023_2 = cargar_texto('Respuestas/Sugerir respuesta/Ejercicio 1 - 2023 -2 .txt')
RespuestaPropuesta_ejercicio_2_2023_2 = cargar_texto('Respuestas/Sugerir respuesta/Ejercicio 2 - 2023 -2 .txt')

# Explicar ejercicio
Nada = ""

# Generar solucion

# Promp para respuesta correcta o incorrecta

PrompCorrectaIncorrecta = cargar_texto('Promp/RespuestaCorrectaIncorrecta.txt')
PrompIdentificarErroresLogicos = cargar_texto('Promp/IdentificaErroresLogicos.txt')
PrompIdentificaErroresSintaxis = cargar_texto('Promp/IdentificaErroresSintaxis.txt')
PrompElementosExtras = cargar_texto('Promp/IdentifcaElementosExtras.txt')
PrompProponersolucion = cargar_texto('Promp/ProponerSolucion.txt')

PrompRespuesta = ""
# -- - - -- - --  PROMPS y casos a resolver - - -- - ---  -- 


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

# Ejecuciones ---------------------------------------------------------

Carpeta = "1.Correctasv4"

# # Base de datos 1 Correcto

# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaCorrecta_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompCorrectaIncorrecta, Carpeta)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaCorrecta_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompCorrectaIncorrecta, Carpeta)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaCorrecta_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompCorrectaIncorrecta, Carpeta)

# # Base de datos 2 Correcto

# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaCorrecta_ejercicio_1_2023_2,"2023_2_E1", "llama3.1", PrompCorrectaIncorrecta, Carpeta)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaCorrecta_ejercicio_2_2023_2,"2023_2_E2", "llama3.1", PrompCorrectaIncorrecta, Carpeta)

# # # ----------------------------------------------------------------

# Carpeta2 = "2.Incorrectasv4"

# # Base de datos 1 incorrecto
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaIncorrecta_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompCorrectaIncorrecta, Carpeta2)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaIncorrecta_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompCorrectaIncorrecta, Carpeta2)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaIncorrecta_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompCorrectaIncorrecta, Carpeta2)

# # Base de datos 2 incorrecto
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaIncorrecta_ejercicio_1_2023_2,"2023_2_E1", "llama3.1", PrompCorrectaIncorrecta, Carpeta2)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaIncorrecta_ejercicio_2_2023_2,"2023_2_E2", "llama3.1", PrompCorrectaIncorrecta, Carpeta2)

# # -------------------------------------------------------------------

Carpeta3 = "3.ErroresLogicosv5"

# # Base de datos 1 Errores logicos
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaErrorLogico_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompIdentificarErroresLogicos, Carpeta3)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaErrorLogico_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompIdentificarErroresLogicos, Carpeta3)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaErrorLogico_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompIdentificarErroresLogicos, Carpeta3)


# # Base de datos 2 Errores logicos
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaErrorLogico_ejercicio_1_2023_2,"2023_2_E1", "llama3.1", PrompIdentificarErroresLogicos, Carpeta3)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaErrorLogico_ejercicio_2_2023_2,"2023_2_E2", "llama3.1", PrompIdentificarErroresLogicos, Carpeta3)


# # ---------------------------------------------------------------------

Carpeta4 = "4.ErroresSintaxisv3"

# # Base de datos 1 Errores Sintaxis
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaErrorSintaxis_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompIdentificaErroresSintaxis, Carpeta4)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaErrorSintaxis_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompIdentificaErroresSintaxis, Carpeta4)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaErrorSintaxis_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompIdentificaErroresSintaxis, Carpeta4)


# # Base de datos 2 Errores Sintaxis
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaErrorSintaxis_ejercicio_1_2023_1,"2023_2_E1", "llama3.1", PrompIdentificaErroresSintaxis, Carpeta4)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaErrorSintaxis_ejercicio_2_2023_1,"2023_2_E2", "llama3.1", PrompIdentificaErroresSintaxis, Carpeta4)


# ---------------------------------------------------------------------

# Carpeta5 = "5.ElementosExtrasV5"

# # Base de datos 1 Identificar elementos adicionales
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaElementosExtras_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompElementosExtras, Carpeta5)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaElementosExtras_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompElementosExtras, Carpeta5)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaElementosExtras_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompElementosExtras, Carpeta5)


# # Base de datos 2 Identificar elementos adicionales
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaElementosExtras_ejercicio_1_2023_2,"2023_2_E1", "llama3.1", PrompElementosExtras, Carpeta5)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaElementosExtras_ejercicio_2_2023_2,"2023_2_E2", "llama3.1", PrompElementosExtras, Carpeta5)


# ---------------------------------------------------------------------

# Carpeta6 = "6.ProponerSolucionV1"

# # Base de datos 1 Proponer solucion con respuesta de estudiante
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaPropuesta_ejercicio_1_2023_1,"2023_1_E1", "llama3.1", PrompProponersolucion, Carpeta6)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaPropuesta_ejercicio_2_2023_1,"2023_1_E2", "llama3.1", PrompProponersolucion, Carpeta6)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, RespuestaPropuesta_ejercicio_3_2023_1,"2023_1_E3", "llama3.1", PrompProponersolucion, Carpeta6)



# # Base de datos 2 Proponer solucion con respuesta de estudiante
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, RespuestaPropuesta_ejercicio_1_2023_2,"2023_2_E1", "llama3.1", PrompProponersolucion, Carpeta6)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, RespuestaPropuesta_ejercicio_2_2023_2,"2023_2_E2", "llama3.1", PrompProponersolucion, Carpeta6)


# ---------------------------------------------------------------------

Carpeta7 = "7.RespuestaCreadaV1"

# # Base de datos 1 Crear Respuesta
# enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, Nada,"2023_1_E1", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, Nada,"2023_1_E2", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_1, Ejercicio3_2023_1, Nada,"2023_1_E3", "llama3.2", PrompRespuesta, Carpeta7)



# # Base de datos 2 Crear Respuesta
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, Nada,"2023_2_E1", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, Nada,"2023_2_E2", "llama3.2", PrompRespuesta, Carpeta7)


# # ---------------------------------------------------------------------

Carpeta8 = "8.ExplicarEjerciciosV1"

# # Base de datos 1 Explicar ejercicio
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, Nada,"2023_2_E1", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, Nada,"2023_2_E2", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, Nada,"2023_2_E1", "llama3.2", PrompRespuesta, Carpeta7)



# # Base de datos 2 Explicar ejercicio
# enviar_prompt(Contexto2023_2, Ejercicio1_2023_2, Nada,"2023_2_E1", "llama3.2", PrompRespuesta, Carpeta7)
# enviar_prompt(Contexto2023_2, Ejercicio2_2023_2, Nada,"2023_2_E2", "llama3.2", PrompRespuesta, Carpeta7)

