# scripts/generate_audio.py
import argparse
import os
from TTS.api import TTS

def main():
    parser = argparse.ArgumentParser(description="Gera áudio com a biblioteca TTS da Coqui.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--config_path", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print("Carregando o modelo TTS...")
    # Inicializa o TTS com os caminhos do modelo
    tts = TTS(model_path=args.model_path, config_path=args.config_path)
    print("Modelo carregado.")

    print(f"Gerando áudio para o arquivo: {args.output_file}")
    # Gera o áudio para o arquivo
    tts.tts_to_file(text=args.text, file_path=args.output_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
