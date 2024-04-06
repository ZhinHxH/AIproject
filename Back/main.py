from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.controllers import link_controller

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(link_controller.router)