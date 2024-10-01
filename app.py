from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
sellers = []
products = []
orders = []

# Add a root route to avoid the 404 error
@app.route('/')
def index():
    return 'Welcome to the Seller Service API!'

# Register a new seller
@app.route('/seller/register', methods=['POST'])
def register_seller():
    data = request.json
    new_seller = {
        'name': data['name'],
        'email': data['email']
    }
    sellers.append(new_seller)
    return jsonify({"message": "Seller registered successfully."}), 201

# Retrieve product details
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['product_id'] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# Update product information
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = next((p for p in products if p['product_id'] == product_id), None)
    if product:
        product.update(data)
        return jsonify({"message": "Product updated successfully."}), 200
    return jsonify({"error": "Product not found"}), 404

# Get all orders for seller’s products
@app.route('/seller/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# Fulfill an order
@app.route('/order/<int:order_id>/fulfill', methods=['PUT'])
def fulfill_order(order_id):
    order = next((o for o in orders if o['order_id'] == order_id), None)
    if order:
        order['status'] = 'fulfilled'
        return jsonify({"message": "Order fulfilled."}), 200
    return jsonify({"error": "Order not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)