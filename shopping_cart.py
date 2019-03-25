class ShoppingCart:
    
    def __init__(self, employee_discount=None):
        self.total = 0
        self.items = []
        self.employee_discount = employee_discount
    
    def add_item(self, name, price, quantity=1):
        self.items.append({"Item": name, "Price": price, "Quantity": quantity})
        self.total += price*quantity
        return self.total

    def mean_item_price(self):
        num_items = len(self.items)
        return sum([item["Price"] for item in self.items])/num_items

    def median_item_price(self):
        prices = sorted([item["Price"] for item in self.items])
        length = len(prices)
        if (length%2 == 0):
            mid_one = length/2
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length)
        return prices[mid]


    def apply_discount(self):
        if self.employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        return self.total*((100-self.employee_discount)/100)

    def void_last_item(self):
        if len(self.items) > 0:
            void_value = self.items.pop()["Price"]
            self.total -= void_value
        else:
            return "There are no items in your cart!"
                