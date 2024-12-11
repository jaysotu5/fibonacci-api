from flask import Blueprint, jsonify

# Define a blueprint named 'fibonacci'
fibonacci_blueprint = Blueprint('fibonacci', __name__)

# Function to calculate Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Route to get the Fibonacci number
@fibonacci_blueprint.route('/<n>', methods=['GET'])
def get_fibonacci(n):
    n = int(n)
    if n < 0:
        return jsonify({'error': 'Input must be a non-negative integer'}), 400
    result = fibonacci(n)
    return jsonify({f'fibonacci({n})': result})
