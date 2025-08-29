# scripts/generate_audio.py
import argparse
from TTS.api import TTS
import os

def main():
    # --- A PARTE QUE FALTAVA ---
    parser = argparse.ArgumentParser(description="Gera áudio com a biblioteca TTS da Coqui.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--model", required=True, help="Caminho para o arquivo do modelo .onnx.")
    parser.add_argument("--config", required=True, help="Caminho para o arquivo de configuração .json.")
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print(f"Carregando o modelo: {args.model}")
    # Inicializa o TTS com os caminhos do modelo
    tts = TTS(model_path=args.model, config_path=args.config)
    print("Modelo carregado.")

    print(f"Gerando áudio para o arquivo: {args.output_file}")
    # Gera o áudio para o arquivo
    tts.tts_to_file(text=args.text, file_path=args.output_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
