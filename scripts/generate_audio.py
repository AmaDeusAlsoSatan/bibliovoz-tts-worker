# scripts/generate_audio.py
import argparse
import os
import wave
import json  # Importa a biblioteca JSON
from piper import PiperVoice

def main():
    parser = argparse.ArgumentParser(description="Gera áudio com Piper TTS.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--config", required=True) 
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print(f"Carregando modelo Piper: {args.model}")

    # CORREÇÃO: Carrega o arquivo de configuração JSON manualmente
    with open(args.config, "r") as config_file:
        config = json.load(config_file)
    
    # Passa o objeto de configuração carregado com o argumento nomeado 'config'
    voice = PiperVoice(args.model, config=config)
    
    print("Modelo carregado.")

    print(f"Gerando áudio para: {args.output_file}")
    with wave.open(args.output_file, "wb") as audio_file:
        voice.synthesize(args.text, audio_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
