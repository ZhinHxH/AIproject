from fastapi import APIRouter, HTTPException
from app.models.link_model import Link
from app.services.link_service  import LinkService


router = APIRouter()
service = LinkService()

@router.get("/identifyUrl")
async  def create():
    result = LinkService.get(self='')
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron enlaces")
    return result

@router.post("/identifyUrl")
async def create(url: Link):
    result = LinkService.post(self='', url=url)
    return result
