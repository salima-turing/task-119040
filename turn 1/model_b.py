from flask import Flask, request, jsonify
from ratelimit import RateLimit, limits

app = Flask(__name__)

# Dummy data for simulation
data_store = [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}]

# Define rate limit settings - 5 requests per minute
limiter = RateLimit(limit=5, per=60)

@app.route('/api/products', methods=['GET'])
@limits(limiter)
def get_products():
    # Simulate API processing time
    # import time
    # time.sleep(0.5)

    response = jsonify(data_store)
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(debug=True)
