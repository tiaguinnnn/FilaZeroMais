#!/usr/bin/env python
import os
import sys

def main():
    # O Django precisa saber onde estão as configurações
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Verifique sua venv!"
        ) from exc

    # Executa o comando (isso vai gerar o link http://127.0.0.1:8000)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Rodar o provisionamento antes de iniciar o servidor
    try:
        from init_db import configurar_banco
        configurar_banco()
    except Exception as e:
        print(f"Aviso: Script init_db.py não executado: {e}")
        
    main()