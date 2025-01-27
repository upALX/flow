import os

c = get_config()  # type: ignore


# Defina o diretório do notebook
c.NotebookApp.notebook_dir = os.getcwd()

# Configure o ambiente virtual para este projeto
venv_path = os.path.join(os.getcwd(), ".venv", "bin", "python")
if os.path.exists(venv_path):
    os.environ["PYTHONPATH"] = venv_path
else:
    print("Aviso: Ambiente virtual não encontrado.")
