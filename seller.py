class Seller:
    def __init__(self, seller_id, name, email):
        self.seller_id = seller_id
        self.name = name
        self.email = email
        self.products = []
        self.order_history = []

    def register_seller(self, name, email):
        # Code to register a new seller
        pass

    def login_seller(self, email, password):
        # Code for seller login
        pass

    def list_products(self):
        # Return the list of products for this seller
        return self.products

    def add_product(self, product):
        # Add a new product to the seller's product list
        self.products.append(product)

    def remove_product(self, product_id):
        # Remove a product from the seller's list
        self.products = [p for p in self.products if p.product_id != product_id]

    def get_order_history(self):
        # Return the order history
        return self.order_history

    def fulfill_order(self, order_id):
        # Fulfill an order and update its status
        pass

    def update_product(self, product_id, name=None, price=None, stock=None):
        # Update product details
        for product in self.products:
            if product.product_id == product_id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if stock:
                    product.stock = stock