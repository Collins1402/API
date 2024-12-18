# Version: 1.0
from flask import Flask, request, jsonify

'''Building a REST API Using Python
a) REST API Setup:
Build a simple REST API in Python using any Python web framework or a custom HTTP
server. The API should manage a Product resource with the following fields:
• name: Product name (string)
• description: Product description (string)
• price: Product price (float)
b) API Endpoints:
Create endpoints to handle:
• POST /products: Accepts a JSON object to create a new product.
• GET /products: Retrieves a list of all products as JSON.
c) Handling Requests and Responses:

Each endpoint should handle JSON requests and responses, including appropriate HTTP
status codes and error handling. Ensure the following behaviors:
• Respond with 201 Created for successful creation of a product.
• Respond with 400 Bad Request if the input data is invalid.
d) Client Interaction Script:
Write a Python script using the requests library to interact with your API endpoints. This
script should:
• Add new products by sending JSON data to the /products endpoint.
• Retrieve and print the list of all products by accessing the /products endpoint.
e) Documentation and Setup Instructions:
Create a README.md file with detailed instructions for:
• Setting up the environment and running the API server.
• Testing the API endpoints manually or with the provided Python script.
Upload your project, including all code and documentation, to a GitHub repository.'''


app = Flask(__name__)

products = []

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Invalid data'}), 400
    product = {
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)