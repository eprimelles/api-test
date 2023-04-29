

def process_orders(orders : list, 
                   criterion : str):
    
    
    revenue = 0
    if criterion == "all":
        for ord in orders:
            revenue += ord.price * ord.quantity
        return revenue
    for ord in orders:
            
            if ord.status == criterion:
                
                revenue += ord.price * ord.quantity
    return revenue
    