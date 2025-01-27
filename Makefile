setup:
	python -m venv .venv
	. .venv/bin/activate && pip install notebook ipykernel && python setup_jupyter.py

run:
	. .venv/bin/activate && jupyter notebook
