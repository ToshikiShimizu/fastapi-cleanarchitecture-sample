from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    item_name: str
    price: float