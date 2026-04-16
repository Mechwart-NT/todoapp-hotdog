@echo on
cd /d %~dp0

echo ========================
echo Backend setup
echo ========================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python nincs telepitve.
    pause
    exit /b
)

if not exist .venv (
    echo Virtual environment letrehozasa...
    python -m venv .venv
)

echo.
echo Virtual environment aktivalasa...
call .venv\Scripts\activate

echo.
echo Fuggosegek telepitese...
pip install -r requirements.txt

echo Migraciok futtatasa...

set FIRST_RUN=0

if not exist db.sqlite3 (
    set FIRST_RUN=1
)

python manage.py makemigrations
python manage.py migrate

if %FIRST_RUN%==1 (
    echo Admin user letrehozasa...
    python manage.py createsuperuser
)

echo.
echo Backend kesz.
pause