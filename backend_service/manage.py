#!/usr/bin/env python
import sys
from database import init_db

def main():
    if len(sys.argv) < 2:
        print("Uso: python manage.py [comando]")
        print("Comandos disponíveis:")
        print("  migrate - Criar tabelas no banco de dados")
        return
    
    command = sys.argv[1]
    
    if command == 'migrate':
        print("Criando tabelas no banco de dados...")
        init_db()
        print("Tabelas criadas com sucesso!")
    else:
        print(f"Comando desconhecido: {command}")

if __name__ == '__main__':
    main()
