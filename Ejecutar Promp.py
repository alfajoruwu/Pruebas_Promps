import requests
import json

# Función para cargar texto desde archivos
def cargar_texto(archivo):
    with open(archivo, 'r') as file:
        return file.read().strip()

# --- Contexto Base de datos ---

Contexto2023_1 = cargar_texto('Contextos/Datos2023-1.txt')
Contexto2023_2 = cargar_texto('Contextos/Datos2023-2.txt')

# --- Enunciados --- 

Ejercicio1_2023_1 = cargar_texto('Ejercicios/Ejercicio 1 2023-1.txt')
Ejercicio2_2023_1 = cargar_texto('Ejercicios/Ejercicio 1 2023-1.txt')
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


# Generar solucion


# -- - - -- - --  PROMPS y casos a resolver - - -- - ---  -- 

# Promp para respuesta correcta o incorrecta

PrompCorrectaIncorrecta = cargar_texto('Promp/RespuestaCorrectaIncorrecta.txt')
PrompIdentificarErroresLogicos = cargar_texto('Promp/IdentificaErroresLogicos.txt')


def enviar_prompt(contexto, enunciado, respuesta, modelo, nombre_archivo, prompt_template):
    prompt = prompt_template.format(
        contexto=contexto,
        enunciado=enunciado,
        respuesta=respuesta,
    )

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
    print(f"Ejecutando prompt en {modelo}...")

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Guardar en txt
    if response.status_code == 200:
        respuesta_llm = response.json().get('response', 'No se recibió una respuesta válida')
        with open(nombre_archivo, 'w') as file:
            file.write(f"""
---------- Respuesta LLM: {modelo}------------------
{respuesta_llm}
""")
        print(f"Respuesta LLM guardada en '{nombre_archivo}'")
    else:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)

# Ejecuciones ---------------------------------------------------------

# ejercicio 1 Correcto|Incorrecto
enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaCorrecta_ejercicio_1_2023_1, "llama3.2", "LLama3.2_Caso_Correcto_ejercicio1.txt", PrompCorrectaIncorrecta)
enviar_prompt(Contexto2023_1, Ejercicio1_2023_1, RespuestaIncorrecta_ejercicio_1_2023_1, "llama3.2", "LLama3.2_Caso_incorrecto_ejercicio1.txt", PrompCorrectaIncorrecta)

# ejercicio 2 Correcto|Incorrecto
enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaCorrecta_ejercicio_2_2023_1, "llama3.2", "LLama3.2_Caso_incorrecto_ejercicio1.txt", PrompCorrectaIncorrecta)
enviar_prompt(Contexto2023_1, Ejercicio2_2023_1, RespuestaIncorrecta_ejercicio_2_2023_1, "llama3.2", "LLama3.2_Caso_incorrecto_ejercicio1.txt", PrompCorrectaIncorrecta)
