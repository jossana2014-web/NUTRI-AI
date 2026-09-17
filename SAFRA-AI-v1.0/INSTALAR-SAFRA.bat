@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ===========================================
echo SAFRA-AI - INSTALACAO
echo ===========================================
python --version
if errorlevel 1 (
  echo Python nao encontrado.
  pause
  exit /b 1
)
if not exist .venv (
  python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
echo.
echo Instalacao concluida.
echo Execute VERIFICAR-SAFRA.bat.
pause
