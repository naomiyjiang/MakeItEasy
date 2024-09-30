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
        self.stock += quantity

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