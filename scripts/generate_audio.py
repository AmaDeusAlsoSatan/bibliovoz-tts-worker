# scripts/generate_audio.py
import argparse
import os
from piper import PiperVoice

def main():
    parser = argparse.ArgumentParser(description="Gera áudio com Piper TTS.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--model", required=True)
    # O argumento --config não é mais necessário, a biblioteca o infere.
    # parser.add_argument("--config", required=True) 
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print(f"Carregando modelo Piper: {args.model}")
    
    # A inicialização foi corrigida. A biblioteca encontra o .json sozinha.
    voice = PiperVoice(args.model)
    
    print("Modelo carregado.")

    print(f"Gerando áudio para: {args.output_file}")
    with open(args.output_file, "wb") as audio_file:
        voice.synthesize(args.text, audio_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
