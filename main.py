from fastapi import FastAPI
from .models.orders import Order
from solutions import process_orders
from pydantic import ValidationError

app = FastAPI()

@app.get("/")
async def root():
    return {
        'message' : 'Hello World'
    }

@app.post("/solutions")
async def post_solutions(orders : dict) -> dict:
    ordrs = []
    for order in orders['orders']:
        try:
            ord = Order(
            id= order["id"],
            item=order["item"],
            quantity=order["quantity"],
            price=order["price"],
            status=order["status"]
            )
            ordrs.append(ord)  
        except ValidationError as e:
            print('Validation error', e)
        
            return {
                'status' : 400,
                'message' : f'Bad order. Order id : {order["id"]}'
            }
        
    return {
        'status' : 200,
        'message' : process_orders(ordrs, orders['criterion'])
    }