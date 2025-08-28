# scripts/upload_to_github.py
import argparse
import os
import subprocess
import shutil

def run_command(command, working_dir="."):
    print(f"Executando em '{working_dir}': {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True, cwd=working_dir)
    if result.returncode != 0:
        print(f"Erro stdout: {result.stdout}")
        print(f"Erro stderr: {result.stderr}")
        raise Exception(f"Comando falhou: {' '.join(command)}")
    print(result.stdout)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_file", required=True)
    parser.add_argument("--repo_owner", required=True)
    parser.add_argument("--repo_name", required=True)
    parser.add_argument("--dest_path", required=True)
    parser.add_argument("--github_token", required=True)
    args = parser.parse_args()

    repo_url = f"https://x-access-token:{args.github_token}@github.com/{args.repo_owner}/{args.repo_name}.git"
    repo_dir = "audio_storage_repo"

    # 1. Clona o repositório
    run_command(["git", "clone", repo_url, repo_dir])

    # 2. Cria a estrutura de pastas e move o arquivo
    dest_full_path = os.path.join(repo_dir, args.dest_path)
    os.makedirs(os.path.dirname(dest_full_path), exist_ok=True)
    shutil.move(args.local_file, dest_full_path)

    # 3. Executa os comandos Git a partir do diretório do repositório clonado
    run_command(["git", "config", "user.email", "action@github.com"], working_dir=repo_dir)
    run_command(["git", "config", "user.name", "GitHub Action TTS Worker"], working_dir=repo_dir)
    run_command(["git", "lfs", "install"], working_dir=repo_dir)
    run_command(["git", "lfs", "track", "*.wav"], working_dir=repo_dir)
    run_command(["git", "add", ".gitattributes"], working_dir=repo_dir)
    # Adiciona o arquivo usando um caminho relativo ao repo_dir
    run_command(["git", "add", args.dest_path], working_dir=repo_dir)
    run_command(["git", "commit", "-m", f"Add audio for {args.dest_path}"], working_dir=repo_dir)
    run_command(["git", "push"], working_dir=repo_dir)

    # 4. Gera a URL pública
    public_url = f"https://media.githubusercontent.com/media/{args.repo_owner}/{args.repo_name}/main/{args.dest_path}"
    print(f"Arquivo disponível em: {public_url}")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"audio_url={public_url}\n")

if __name__ == "__main__":
    main()
