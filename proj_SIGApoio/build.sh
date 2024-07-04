#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalação das dependências usando pip
pip install -r ./requirements.txt

# Comandos de gerenciamento do Django
python manage.py collectstatic --no-input
python manage.py migrate