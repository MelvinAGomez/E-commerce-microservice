from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

orders = []

@app.route('/', methods=['GET'])
def home_products():
    return render_template('order_home.html')

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    orders.append(data)
    return jsonify({"message": "Order added successfully"}), 201

# Additional routes for order management

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
