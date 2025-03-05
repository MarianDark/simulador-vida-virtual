import os
import openai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar la API Key de OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("No se encontró la clave API de OpenAI. Agrega OPENAI_API_KEY en el archivo .env.")

openai.api_key = OPENAI_API_KEY

def generate_npc_decision(prompt: str) -> str:
    """
    Genera una decisión para el NPC basada en el prompt proporcionado.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Puedes cambiarlo por otro modelo como GPT-4
            messages=[{"role": "system", "content": "Eres un NPC en un simulador de vida virtual y tomas decisiones inteligentes."},
                      {"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error con OpenAI: {e}")
        return "No se pudo generar una decisión."
