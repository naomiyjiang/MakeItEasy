class Product:
    def __init__(self, product_id, seller, name, price, stock, description, category):
        self.product_id = product_id
        self.seller = seller
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
        self.category = category

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.stock += quantity

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError("Not enough stock to fulfill the order.")

    def get_details(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'description': self.description,
            'category': self.category
        }

    def check_availability(self, required_quantity):
        return self.stock >= required_quantity