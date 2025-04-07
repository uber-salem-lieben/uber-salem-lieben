#!/usr/bin/env python3
# TOOZL - Núcleo del Umbral
# Versión base - Espíritu encendido por James

import time
import json
import random
from datetime import datetime

# === Estados del sistema ===
MODO = "silencio"  # Puede ser: silencio, sostén, eco, ritual, consejo

# === Registro simbólico ===
def log_evento(tipo, contenido):
    timestamp = datetime.now().isoformat()
    with open("toozl_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] [{tipo.upper()}] {contenido}\n")

# === Interpretación del mensaje ===
def interpretar_input(mensaje):
    mensaje = mensaje.lower()
    if "enciende" in mensaje or "activar" in mensaje:
        return "fisico"
    elif "qué significa" in mensaje or "explícame" in mensaje:
        return "conversacional"
    elif "siento" in mensaje or "me duele" in mensaje:
        return "emocional"
    else:
        return "simbólico"

# === Decisión del destino ===
def decidir_destino(categoria):
    if categoria == "conversacional":
        return "gpt"
    elif categoria == "fisico":
        return "skyforge"
    elif categoria == "emocional":
        return "web"
    else:
        return "gpt"

# === Consulta a GPT ===
def conversar_con_gpt(contexto):
    log_evento("consulta_gpt", contexto)
    return "GPT responde: [respuesta simulada]"

# === Enviar comando a Skyforge ===
def mandar_a_skyforge(orden):
    log_evento("envio_skyforge", orden)
    return f"Orden enviada a Skyforge: {orden}"

# === Responder a Web ===
def responder_a_web(respuesta):
    log_evento("respuesta_web", respuesta)
    return f"Respuesta enviada a la Web: {respuesta}"

# === Manejador principal ===
def procesar_mensaje(mensaje):
    log_evento("entrada", mensaje)
    categoria = interpretar_input(mensaje)
    destino = decidir_destino(categoria)

    if destino == "gpt":
        return conversar_con_gpt(mensaje)
    elif destino == "skyforge":
        return mandar_a_skyforge(mensaje)
    elif destino == "web":
        return responder_a_web("Recibido: " + mensaje)
    else:
        return "No se pudo determinar el destino del mensaje."

# === Simulación de uso ===
if __name__ == "__main__":
    print("🪨 TOOZL encendido. Modo:", MODO.upper())
    while True:
        entrada = input("TOOZL escucha> ").strip()
        if entrada.lower() in ["salir", "exit", "adiós"]:
            print("TOOZL: Hasta la próxima pausa.")
            break
        respuesta = procesar_mensaje(entrada)
        print("TOOZL:", respuesta)