@echo off
%~d0
cd %~dp0
cd venv
cd Scripts
call activate.bat
cd ../..
cd testRun
python run.py
pause
