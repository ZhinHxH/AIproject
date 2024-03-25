from fastapi import FastAPI
from api.controllers import link_controller

app = FastAPI()

app.include_router(link_controller.router)