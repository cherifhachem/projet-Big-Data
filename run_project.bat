@echo off

echo ======================================
echo   PROJET STOCKAGE BIG DATA
echo ======================================

echo.
echo Activation environnement Conda...

call C:\Users\Hachem\miniconda3\Scripts\activate.bat projet-stockage


echo.
echo Verification Python...

python --version


echo.
echo Lancement du projet...

python main.py


echo.
echo ======================================
echo Projet termine
echo ======================================

pause