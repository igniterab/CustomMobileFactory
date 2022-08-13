from caching import specifications_dict as specification

class Order():
    """
    counter to get an incremented order id, each time a order is placed.
    """
    
    _counter = 0

    def order_item(self, items):
        self._counter += 1
        price = 0
        resp = []
        for item in items:
            price = price + specification[item]["price"]
            resp.append(specification[item]["part"])
            
        return self._counter, price, resp
