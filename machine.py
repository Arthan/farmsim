class Machine():
    def __init__(self, name='', engine=0, speed=0, weight=0, price=0, wait=0):
        self.name = name
        self.engine = engine
        self.speed = speed
        self.weight = weight
        self.price = price
        self.wait = wait

    def __str__(self) -> str:
        price_str = f'{self.price:,.0f}'.replace(',', '.')
        return f'{self.name} => {self.engine}KM | {self.speed}km/h | {self.weight}t | [${price_str}]'

