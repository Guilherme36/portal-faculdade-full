@echo off
cd backend_service
set DATABASE_URL=sqlite:///turmas.db
..\\.venv\Scripts\python server.py
