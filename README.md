El repo contiene 3 servicios:

# Servicio de Mysql
Contine un script que se corre e instala con unos registros de prueba
# Servicio de ETL
Contiene una transformacion de los datos, obtiene un csv de la carpeta etl el cual se cruza con los datos de maysql y desplegados en la carpeta bucket.
# Servicio de API
Encargado de disponibilizar los datos de la carpeta bucket en un api sencillo. Los logs se guardan en ruta api/logs.
# Servicio de CICD en Jenkins: 
    - Creación de entorno virtual
    - Instalación de dependencias
    - Validación de sintaxis con Flake8
    - Ejecución de pruebas con Pytest
    - Generación de documentación con Pdoc 
## Descripción del Pipeline

El `Jenkinsfile` define un pipeline con las siguientes etapas:

1. **Crear entorno virtual e instalar dependencias**
   - Se crea un entorno virtual Python (`.venv`).
   - Se instalan las dependencias definidas en `requirements.txt`.

2. **Validar sintaxis**
   - Se ejecuta `flake8` para verificar la calidad del código en `src/` y `tests/`.

3. **Ejecutar pruebas**
   - Se ejecutan las pruebas unitarias y de integración con `pytest`.
   - Se genera un archivo XML (`tests/results.xml`) para que Jenkins pueda procesar los resultados.

4. **Generar documentación**
   - Se usa `pdoc` para generar documentación HTML en la carpeta `docs/`.

# Docker Compose 

El docker compose principal orquesta para que se publiquen los 4 servicios.