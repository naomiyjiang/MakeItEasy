from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from seller import Seller
from product import Product


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dbuserdbuser@34.173.164.27/Seller_Service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create the tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Welcome to the Seller Service API!'


# Test database connection route
@app.route('/test-db-connection', methods=['GET'])
def test_db_connection():
    try:
        sellers = Seller.query.all()
        return jsonify({"message": "Database connection successful", "sellers": len(sellers)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Register a new seller
@app.route('/seller/register', methods=['POST'])
def register_seller():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    new_seller = Seller(name=name, email=email)
    db.session.add(new_seller)
    db.session.commit()

    return jsonify(new_seller.register_seller()), 201

# Create a new product
@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    seller_id = data.get('seller_id')
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')
    description = data.get('description')
    category = data.get('category')

    seller = Seller.query.get(seller_id)
    if not seller:
        return jsonify({"error": "Seller not found"}), 404

    new_product = Product(seller_id=seller.id, name=name, price=price, stock=stock, description=description, category=category)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created successfully.", "product_id": new_product.id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

'''@app.route('/test-db-connection', methods=['GET'])
def test_db_connection():
    try:
        # Attempt to query the Seller table to check the connection
        sellers = Seller.query.all()  # Query all sellers
        return jsonify({"message": "Successfully connected to the database!", "sellers": len(sellers)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a root route to avoid the 404 error
@app.route('/')
def index():
    return 'Welcome to the Seller Service API!'

# Register a new seller
@app.route('/seller/register', methods=['POST'])
def register_seller():
    global seller_id_counter
    data = request.json
    name = data.get('name')
    email = data.get('email')

    new_seller = Seller(seller_id_counter, name, email)
    sellers[seller_id_counter] = new_seller
    seller_id_counter += 1

    return jsonify(new_seller.register_seller(name, email)), 201

@app.route('/product', methods=['POST'])
def create_product():
    global product_id_counter
    data = request.json
    seller_id = data.get('seller_id')
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')
    description = data.get('description')
    category = data.get('category')

    if seller_id not in sellers:
        return jsonify({"error": "Seller not found"}), 404

    new_product = Product(product_id_counter, sellers[seller_id], name, price, stock, description, category)
    products[product_id_counter] = new_product
    sellers[seller_id].add_product(new_product)
    product_id_counter += 1

    return jsonify({"message": "Product created successfully.", "product_id": new_product.product_id}), 201

# Route to get product details
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = products.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product.get_details()), 200

# Route to update stock
@app.route('/product/<int:product_id>/stock', methods=['PUT'])
def update_stock(product_id):
    product = products.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.json
    quantity = data.get('quantity', 0)

    try:
        product.update_stock(quantity)
        return jsonify({"message": "Stock updated successfully."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Route to check product availability
@app.route('/product/<int:product_id>/availability', methods=['GET'])
def check_availability(product_id):
    product = products.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    required_quantity = int(request.args.get('quantity', 1))

    if product.check_availability(required_quantity):
        return jsonify({"available": True, "message": "Product is available."}), 200
    else:
        return jsonify({"available": False, "message": "Not enough stock."}), 200
'''
