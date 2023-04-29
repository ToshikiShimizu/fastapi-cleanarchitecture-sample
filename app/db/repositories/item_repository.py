from app.db.connection import get_connection
from app.domain.entities.item import Item   

def get_item(item_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT item_id, item_name, price FROM items WHERE item_id = ?", (item_id,))
    item = cursor.fetchone()

    conn.close()
    
    if item:
        return Item(item_id=item[0], item_name=item[1], price=item[2])
    else:
        return None