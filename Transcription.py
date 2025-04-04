import whisper
import os
import logging
import time

# --- CONFIGURAÇÃO DE LOGS ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# --- CONFIGURAÇÕES ---
AUDIO_FILE = "audio_2025-04-03_19-08-41.mp3"  # nome do arquivo de áudio no mesmo diretório
OUTPUT_FILE = "transcricao_" + os.path.splitext(AUDIO_FILE)[0] + ".txt"  # nome do arquivo de saída

# --- FUNÇÃO DE TRANSCRIÇÃO COM WHISPER ---
def transcrever(audio_path):
    logger.info("Iniciando transcrição...")
    start_time = time.time()

    # Verificando se o arquivo de áudio existe antes de tentar carregar
    if not os.path.exists(audio_path):
        logger.error(f"Arquivo de áudio {audio_path} não encontrado!")
        return ""
    
    # Carregando o modelo Whisper
    logger.info("Carregando o modelo Whisper...")
    model_start_time = time.time()
    model = whisper.load_model("medium")  # pode mudar para "small", "medium", "large"
    model_end_time = time.time()
    logger.info(f"Modelo carregado com sucesso em {model_end_time - model_start_time:.2f} segundos!")
    
    # Carregando o arquivo de áudio
    logger.info(f"Carregando o áudio do arquivo {audio_path}...")
    audio_start_time = time.time()
    result = model.transcribe(audio_path)
    audio_end_time = time.time()
    logger.info(f"Áudio carregado e processado em {audio_end_time - audio_start_time:.2f} segundos!")

    # Finalização do processo
    end_time = time.time()
    logger.info(f"Transcrição concluída em {end_time - start_time:.2f} segundos!")
    
    # Retorna o texto transcrito
    return result["text"]

# --- FUNÇÃO PARA SALVAR A TRANSCRIÇÃO EM UM ARQUIVO TXT ---
def salvar_transcricao(texto, output_path):
    logger.info(f"Salvando transcrição no arquivo {output_path}...")
    start_time = time.time()
    with open(output_path, 'w') as file:
        file.write(texto)
    end_time = time.time()
    logger.info(f"Transcrição salva com sucesso em {output_path} em {end_time - start_time:.2f} segundos!")

# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    if not os.path.exists(AUDIO_FILE):
        logger.error(f"Arquivo {AUDIO_FILE} não encontrado!")
    else:
        # Etapa de transcrição
        logger.info("\nIniciando o processo de transcrição do áudio...")
        texto_transcrito = transcrever(AUDIO_FILE)
        if texto_transcrito:
            logger.info(f"\nTexto Transcrito:\n{texto_transcrito}\n")

            # Etapa de salvar o arquivo
            salvar_transcricao(texto_transcrito, OUTPUT_FILE)