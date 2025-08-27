import argparse
import os
import subprocess

def run_command(command):
    """Executa um comando no shell e imprime a saída."""
    print(f"Executando: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao executar comando: {result.stderr}")
        raise Exception(f"Comando falhou: {' '.join(command)}")
    print(result.stdout)

def main():
    parser = argparse.ArgumentParser(description="Faz upload de um arquivo para um repositório GitHub via commit.")
    parser.add_argument("--local_file", required=True)
    parser.add_argument("--repo_owner", required=True)
    parser.add_argument("--repo_name", required=True)
    parser.add_argument("--dest_path", required=True)
    parser.add_argument("--github_token", required=True)
    args = parser.parse_args()

    repo_url = f"https://x-access-token:{args.github_token}@github.com/{args.repo_owner}/{args.repo_name}.git"
    repo_dir = "audio_storage_repo"

    # 1. Clona o repositório de armazenamento
    run_command(["git", "clone", repo_url, repo_dir])

    # 2. Move o arquivo de áudio para o diretório de destino
    dest_full_path = os.path.join(repo_dir, args.dest_path)
    os.makedirs(os.path.dirname(dest_full_path), exist_ok=True)
    os.rename(args.local_file, dest_full_path)

    # 3. Configura o Git LFS, faz commit e push
    os.chdir(repo_dir)
    run_command(["git", "config", "--global", "user.email", "action@github.com"])
    run_command(["git", "config", "--global", "user.name", "GitHub Action TTS Worker"])
    run_command(["git", "lfs", "install"])
    run_command(["git", "lfs", "track", "*.wav"])
    run_command(["git", "add", ".gitattributes"])
    run_command(["git", "add", dest_full_path])
    run_command(["git", "commit", "-m", f"Add audio for {args.dest_path}"])
    run_command(["git", "push"])
    os.chdir("..")

    # 4. Gera a URL pública para o Firestore
    public_url = f"https://media.githubusercontent.com/media/{args.repo_owner}/{args.repo_name}/main/{args.dest_path}"
    print(f"Arquivo disponível em: {public_url}")
    # Forma padrão do GitHub Actions para passar saídas entre passos
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"audio_url={public_url}\n")


if __name__ == "__main__":
    main()
