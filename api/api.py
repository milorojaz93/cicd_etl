from fastapi import FastAPI, HTTPException, Request
import pandas as pd
import os
import logging
from fastapi.responses import JSONResponse
from datetime import datetime

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/logs/api.log"),
        logging.StreamHandler()  # opcional, para seguir viendo por consola
    ]
)

app = FastAPI()

PARQUET_DIR = "/data/proveedores"

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).total_seconds()
    logging.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.3f}s")
    return response

@app.get("/proveedor/{nombre}")
def get_proveedor(nombre: str):
    proveedor_path = os.path.join(PARQUET_DIR, f"proveedor={nombre}")

    logging.info(f"Solicitud para proveedor: {nombre}")

    if not os.path.exists(proveedor_path):
        logging.warning(f"No se encontró directorio para proveedor: {nombre}")
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")

    try:
        df = pd.read_parquet(proveedor_path, engine="pyarrow")
        logging.info(f"Leídos {len(df)} registros para proveedor: {nombre}")
        return df.to_dict(orient="records")

    except Exception as e:
        logging.exception(f"Error al leer datos del proveedor {nombre}")
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos del proveedor: {str(e)}")

# Manejo global de errores inesperados
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.exception(f"Excepción inesperada: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno en el servidor."},
    )
