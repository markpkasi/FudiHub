from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for restaurants and menu items (replace with a database)
restaurants = [
    {
        "id": 1,
        "name": "Restaurant A",
        "menu": [
            {"id": 1, "name": "Pizza", "price": 10.99},
            {"id": 2, "name": "Burger", "price": 8.99},
        ],
    },
    {
        "id": 2,
        "name": "Restaurant B",
        "menu": [
            {"id": 3, "name": "Sushi", "price": 12.99},
            {"id": 4, "name": "Pasta", "price": 11.99},
        ],
    },
]

orders = []

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    return jsonify(restaurants)

@app.route("/place-order", methods=["POST"])
def place_order():
    data = request.json
    restaurant_id = data.get("restaurant_id")
    item_id = data.get("item_id")
    quantity = data.get("quantity")
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    item = next((item for item in restaurant["menu"] if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    total_price = item["price"] * quantity
    orders.append({"restaurant": restaurant["name"], "item": item["name"], "quantity": quantity, "total_price": total_price})
    return jsonify({"message": "Order placed successfully"})

if __name__ == "__main__":
    app.run(debug=True)
