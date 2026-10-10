from flask import Flask, jsonify

app = Flask(__name__)

ITEMS = {
    1: {"name": "widget", "stock": 42},
    2: {"name": "gadget", "stock": 7},
}

@app.get("/items")
def list_items():
    return jsonify(list(ITEMS.values()))

@app.get("/items/<int:item_id>")
def get_item(item_id):
    item = ITEMS.get(item_id)
    if item is None:
        return {"error": "not found"}, 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(port=8080)
