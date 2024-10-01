class Seller:
    def __init__(self, seller_id, name, email):
        self.seller_id = seller_id
        self.name = name
        self.email = email
        self.products = []
        self.order_history = []

    def register_seller(self, name, email):
        self.name = name
        self.email = email
        return {"message": "Seller registered successfully.", "seller_id": self.seller_id}

    def login_seller(self, email, password):
        # Code for seller login logic
        if self.email == email:
            return {"message": "Login successful."}
        else:
            return {"error": "Invalid credentials."}

    def list_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def get_order_history(self):
        return self.order_history

    def fulfill_order(self, order_id):
        for order in self.order_history:
            if order.order_id == order_id:
                order.status = "fulfilled"
                return {"message": "Order fulfilled."}
        return {"error": "Order not found."}

    def update_product(self, product_id, name=None, price=None, stock=None):
        for product in self.products:
            if product.product_id == product_id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if stock is not None:
                    product.stock = stock
                return {"message": "Product updated."}
        return {"error": "Product not found."}