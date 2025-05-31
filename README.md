# setup del server -> correr en terminal
1. Clonar repositorio
git clone https://github.com/marcelobv0/dTalent.git
cd dtalent_backend
2. Crear y activar un entorno virtual
python -m venv .venv && source .venv/bin/activate #mac 
python -m venv .venv && source .venv/Scripts/activate #windows
3. instalar dependencias
pip install -r requirements.txt
4. crear un archivo .env
Crear un archivo .env en el directorio base (donde se encuentra el manage.py) con el archivo .env disponible como ejemplo.
5. creación de la base de datos (postgres)
En pg admin o terminal: 
createdb dtalent  ## nombre de la base de datos = dtalent
6. Aplicar Migraciones
python manage.py migrate
7. Importar datos iniciales (opcional)
psql -U postgres -d dtalent -f db_dump.sql 

8. Ejecutar el servidor. correrá en http://localhost:8000.
python manage.py runserver

# toda la información pertinente (a settings) está en el archivo .env


## admin en localhost, puerto 8000: 
username admin pw admin
http://localhost:8000/admin/

## API test - cmd (windows)
1. Post (/users/login/, necesita de usuario y contraseña para autenticación)
curl -X POST "http://localhost:8000/users/login/" -H "Content-Type: application/json" -d "{\"username\": \"test2\", \"password\": \"issatest23\"}"-> retorna token
 cambiar usuario y contraseña dentro de los \\ para probar con distintos usuarios. ej: \"username\": \"u33\", \"password\": \"usuario33\"


## get
1. usuarios (necesita token de autenticación)
curl http://127.0.0.1:8000/users/ \ -H "Authorization: Token {token}" 

2. receipts (necesita token de autenticación)
curl http://127.0.0.1:8000/receipts/?year=2025 \ -H "Authorization: Token {token}"  // con un filtro de año

3. con filtros (necesita token)
curl http://127.0.0.1:8000/users/?nationality=chilean \ -H "Authorization: Token {token}"  // con un filtro de nacionalidad

## Descargo de recibos específicos (necesita token)
curl -H "Authorization: Token {token}" --output recibo2.pdf "http://127.0.0.1:8000/receipts/2/file/" -> descarga el archivo al directorio desde donde se está trabajando con el nombre de "recibo2" y en formato pdf.



#structure 
config/           # settings del django
users/            # auth, tokens, registros
receipts/         # recibos
