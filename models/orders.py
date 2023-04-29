from pydantic import BaseModel, validator, ValidationError


class Order(BaseModel):

    id : int
    item : str
    quantity : int
    price : float
    status : str

    @validator('id')
    def id_validator(cls, v):

        if v < 0: # Not negative
            raise ValueError("Negative id")
        
        return v
    @validator('item')
    def item_validator(cls, v):
        
        if v is None: # None string
            raise ValueError("Item is None")
        
        if len(v) == 0: # Empty
            raise ValueError("Empyt item")
        
        return v.title()
    
    @validator('quantity')
    def quantity_validator(cls, v):

        if v <= 0: # Zero or negative quantity
            raise ValueError("Zero or negative quantity")
        
        if not isinstance(v, int):
            raise ValueError("Not integer quantity")

        return v
    
    @validator('price')
    def price_validator(cls, v):

        if v <= 0:
            raise ValueError("Zero or negative price")
        
        return v
    @validator('status')
    def status_validator(cls, v):

        statuses = ['completed', 'pending', 'canceled']

        if not v in statuses:
            raise ValueError('Invalid Status')
        
        return v

if __name__ == "__main__":

    try:
        o = Order(
        id=4, item='Mouse', quantity=3, price=-23.99, status='pending'
        )
    except ValidationError as e:
        print('Validation error', e) 

    #print(o)