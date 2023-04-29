from pydantic import BaseModel


class Order(BaseModel):

    id : int
    item : str
    quantity : int
    price : float
    status : str

    def validate(self) -> bool:
        if self.id < 0:
            return False
        
        if self.item is None:
            return False
        
        if self.quantity <= 0:
            return False
        
        if self.price <= 0:
            return False

        if self.status is None:
            return False

        return True 