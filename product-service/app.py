from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/") 

db = client["product_db"]  
collection = db["products"]

@app.route('/products', methods=['GET'])
def get_products():
    products = []
    for product in collection.find():
        products.append(product)
    return render_template('products.html', products=products)

@app.route('/', methods=['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))  # Convert price to float
        description = request.form.get('description')

        product = {'name': name, 'price': price, 'description': description}
        collection.insert_one(product)

        return jsonify({'message': 'Product added successfully!'})

    return render_template('product.html')  # Redirect to products page on error

if __name__ == '__main__':
    app.run(port=5000, debug=True)
