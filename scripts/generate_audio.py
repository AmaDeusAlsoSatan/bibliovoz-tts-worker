# scripts/generate_audio.py
import argparse
import os
from piper import PiperVoice

def main():
    parser = argparse.ArgumentParser(description="Gera áudio a partir de texto usando Piper TTS.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--model", required=True, help="Caminho para o arquivo do modelo .onnx.")
    # ADICIONE O NOVO ARGUMENTO
    parser.add_argument("--config", required=True, help="Caminho para o arquivo de configuração .json.")
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    print(f"Carregando modelo: {args.model}")
    print(f"Usando configuração: {args.config}")
    
    # PASSA OS DOIS ARGUMENTOS
    voice = PiperVoice(args.model, config_path=args.config)
    
    print(f"Gerando áudio para o arquivo: {args.output_file}")
    voice.synthesize_wav_file(args.text, args.output_file)
    
    print("Geração de áudio concluída com sucesso.")

if __name__ == "__main__":
    main()
