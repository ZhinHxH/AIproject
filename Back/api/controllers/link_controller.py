from fastapi import APIRouter
from app.models.link_model import Link
from app.services.link_service  import LinkService


router = APIRouter()
service = LinkService()

@router.post("/identifyUrl/")
async def create(url: Link):
    result = LinkService.post(self='', url=url)
    return result

@router.get("/identifyUrl")
async  def create():
    return {"message": "¡La API está en funcionamiento!"}