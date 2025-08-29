import argparse
from TTS.api import TTS
import os

def main():
    parser = argparse.ArgumentParser(description="Gera áudio com a biblioteca TTS da Coqui.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print("Carregando o modelo TTS pré-treinado para português...")
    # O nome do modelo oficial da Coqui para português do Brasil
    model_name = "tts_models/pt/cv/vits"
    
    # A biblioteca TTS lida com o download e o cache do modelo automaticamente
    tts = TTS(model_name)
    print("Modelo carregado.")

    print(f"Gerando áudio para o arquivo: {args.output_file}")
    tts.tts_to_file(text=args.text, file_path=args.output_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
