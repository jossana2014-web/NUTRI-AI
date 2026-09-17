@echo off
chcp 65001 >nul
cd /d "%~dp0"
if exist .venv\Scripts\activate (
  call .venv\Scripts\activate
)
python -m safra diagnostico
pause
