from fastapi import APIRouter, HTTPException
from app.domain.usecases.item_usecase import ItemUsecase
from app.domain.entities.item import Item

router = APIRouter()

@router.get("/item/{item_id}", response_model=Item)
async def get_item_info(item_id: int):
    item = ItemUsecase.get_item_info(item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")
