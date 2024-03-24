from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = []

@app.route('/', methods=['GET'])
def home_products():
    return render_template('user_home.html')

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    # Logic to handle user login
    return jsonify({"message": "User logged in successfully"}), 200

@app.route('/profile/<username>', methods=['GET', 'PUT'])
def profile(username):
    # Logic to handle user profile
    return jsonify({"message": f"Profile of {username}"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
