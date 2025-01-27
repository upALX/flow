import os
import subprocess
import sys

def setup_project_jupyter_kernel():
    # Caminho do ambiente virtual (ajuste se necessário)
    venv_path = os.getenv("VIRTUAL_ENV") or ".venv"
    if not os.path.exists(venv_path):
        print(f"Ambiente virtual '{venv_path}' não encontrado. Certifique-se de que ele está configurado.")
        sys.exit(1)

    python_executable = os.path.join(venv_path, "bin", "python")
    kernel_name = os.path.basename(os.getcwd())  # Nome do kernel baseado na pasta do projeto
    display_name = f"Python ({kernel_name})"

    try:
        # Instalar os pacotes necessários
        subprocess.check_call([python_executable, "-m", "pip", "install", "notebook", "ipykernel"])

        # Registrar o kernel
        subprocess.check_call([
            python_executable, "-m", "ipykernel", "install",
            "--user",
            f"--name={kernel_name}",
            f"--display-name={display_name}"
        ])
        print(f"Kernel do Jupyter para o projeto '{kernel_name}' configurado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar o kernel do Jupyter: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_project_jupyter_kernel()
