from typing import Optional

from app.db.repositories.item_repository import get_item
from app.domain.entities.item import Item


class ItemUsecase:
    @staticmethod
    def get_item_info(item_id: int) -> Optional[Item]:
        item = get_item(item_id)
        if item:
            return item
        else:
            return None
