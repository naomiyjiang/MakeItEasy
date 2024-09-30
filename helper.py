class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].update_stock(quantity)

    def get_product(self, product_id):
        return self.products.get(product_id)

    def check_product_availability(self, product_id, required_quantity):
        product = self.get_product(product_id)
        if product:
            return product.check_availability(required_quantity)
        return False