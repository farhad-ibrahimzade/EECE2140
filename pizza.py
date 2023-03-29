class Pizza:
    
    sizePrice = {
        "small" : 8, 
        "medium": 12,
        "large": 14
    }
    
    def __init__(self, size):
        if size in Pizza.sizePrice:
            self.price = Pizza.sizePrice[size]
            self.size = size
        else:
            raise ValueError("Invalid Size")
        self.toppings = []

    def addTopping(self, topping):
        self.toppings.append(topping)

    def removeTopping(self, topping):
        self.toppings.remove(topping)

    def calculateCost(self):
        return self.price + 2*len(self.toppings)

    def __str__(self) -> str:
        return "Size: " + self.size + ", Toppings: " + str(self.toppings) \
        + ", Price: " + str(self.calculateCost())
