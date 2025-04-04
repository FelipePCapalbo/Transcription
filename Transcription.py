import whisper
import os

# --- CONFIGURAÇÕES ---
AUDIO_FILE = "audio_2025-04-03_19-08-41.mp3"  # nome do arquivo de áudio no mesmo diretório
OUTPUT_FILE = "transcricao_" + os.path.splitext(AUDIO_FILE)[0] + ".txt"  # nome do arquivo de saída

# --- FUNÇÃO DE TRANSCRIÇÃO COM WHISPER ---
def transcrever(audio_path):
    print("Iniciando transcrição...")
    model = whisper.load_model("large")  # pode mudar para "small", "medium", "large"
    result = model.transcribe(audio_path)
    print("Transcrição concluída!")
    return result["text"]

# --- FUNÇÃO PARA SALVAR A TRANSCRIÇÃO EM UM ARQUIVO TXT ---
def salvar_transcricao(texto, output_path):
    with open(output_path, 'w') as file:
        file.write(texto)
    print(f"Transcrição salva em {output_path}")

# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    if not os.path.exists(AUDIO_FILE):
        print(f"Arquivo {AUDIO_FILE} não encontrado!")
    else:
        texto_transcrito = transcrever(AUDIO_FILE)
        print(f"\nTexto Transcrito:\n{texto_transcrito}\n")

        salvar_transcricao(texto_transcrito, OUTPUT_FILE)
