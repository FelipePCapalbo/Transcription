import whisper
import requests
import json
import os

# --- CONFIGURAÇÕES ---
AUDIO_FILE = "Silvia.mp3"  # nome do arquivo de áudio no mesmo diretório
LLM_API_URL = "http://localhost:1234/v1/chat/completions"

# --- FUNÇÃO DE TRANSCRIÇÃO COM WHISPER ---
def transcrever(audio_path):
    print("Iniciando transcrição...")
    model = whisper.load_model("large")  # pode mudar para "small", "medium", "large"
    result = model.transcribe(audio_path)
    print("Transcrição concluída!")
    return result["text"]

# --- ENVIA O TEXTO PARA O LLM LOCAL VIA LM STUDIO ---
def perguntar_llm(texto):
    print("Enviando para o LLM local...")
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "phi-3",  # informativo, LM Studio usa o modelo carregado
        "messages": [
            {"role": "system", "content": "Você é um assistente que resume transcrições de áudio."},
            {"role": "user", "content": f"Resuma o seguinte áudio: {texto}"}
        ],
        "temperature": 0.3,
        "max_tokens": 2048
    }

    response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    print("✅ Resposta recebida do LLM.")
    return response.json()['choices'][0]['message']['content']

# --- PIPELINE COMPLETO ---
def executar_pipeline():
    if not os.path.exists(AUDIO_FILE):
        print(f"Arquivo {AUDIO_FILE} não encontrado!")
        return
    
    texto_transcrito = transcrever(AUDIO_FILE)
    print(f"\nTexto Transcrito:\n{texto_transcrito}\n")

    resposta = perguntar_llm(texto_transcrito)
    print(f"\nResumo do LLM:\n{resposta}\n")

# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    executar_pipeline()
