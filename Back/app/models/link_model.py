from pydantic import BaseModel

class Link(BaseModel):
    url: str
    texto: str
    clasificacion: str