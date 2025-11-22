@echo off
echo ========================================
echo Setup Local - Sistema Gerenciador de Turmas
echo ========================================

echo.
echo [1/5] Instalando dependencias do backend...
cd backend_service
pip install -r requirements.txt

echo.
echo [2/5] Compilando arquivos proto...
python compile_protos.py

echo.
echo [3/5] Copiando arquivos proto para o frontend...
xcopy /Y protos\*.py ..\frontend_service\protos\

echo.
echo [4/5] Instalando dependencias do frontend...
cd ..\frontend_service
pip install -r requirements.txt

echo.
echo [5/5] Criando banco de dados...
cd ..\backend_service
python manage.py migrate

echo.
echo ========================================
echo Setup concluido!
echo ========================================
echo.
echo Para executar:
echo   1. Backend gRPC: cd backend_service ^&^& python server.py
echo   2. Frontend REST: cd frontend_service ^&^& python manage.py runserver
echo   3. Consumer AMQP: cd backend_service ^&^& python consumer.py
echo.
echo Nao esqueca de iniciar o RabbitMQ:
echo   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
echo.
