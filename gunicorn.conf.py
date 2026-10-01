import os

# Adjust these values as needed
bind = "0.0.0.0:8000"  # Host and port for Gunicorn to listen on
# MrDesk: a VM tem ~1 GB de memoria e o rdgen so e usado pelo Celso, de vez em
# quando. 5 workers x 6 threads deixava ~150-200 MB parados. 1 worker com 4 threads
# da conta de gerar builds (inclusive 2 ao mesmo tempo) e receber os exes do GitHub.
workers = 1
threads = 4
activate_base = True  # Activate your virtual environment if applicable

# Path to your Django project's main WSGI application file (usually manage.py)
wsgi_app = "rdgen.wsgi.application"