@echo off
echo 🔥 CONFIGURANDO FILAZERO+ PARA A BANCA...
python init_db.py
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db
echo ✅ TUDO PRONTO! RODE: python manage.py runserver
pause