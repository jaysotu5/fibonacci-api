import logging
from flask import Flask, jsonify

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from fibonacci_blueprint import fibonacci_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(fibonacci_blueprint, url_prefix='/fibonacci')

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Global error handler for catching unhandled exceptions
    @app.errorhandler(Exception)
    def handle_error(error):
        logger.error(f"Unhandled exception: {str(error)}")
        return jsonify({'error': 'Internal Server Error'}), 500

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({'error': 'Bad Request'}), 400

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Not Found'}), 404
    return app

# if __name__ == '__main__':
#     app.run(debug=False)
