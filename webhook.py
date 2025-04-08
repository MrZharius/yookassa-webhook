from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def set_premium(user_id):
    with open("premium_users.txt", "a", encoding="utf-8") as f:
        f.write(f"✅ Premium for user {user_id} at {datetime.now()}\n")

@app.route("/yookassa-webhook", methods=["POST"])
def yookassa_webhook():
    event = request.json
    if event.get("event") == "payment.succeeded":
        user_id = int(event["object"]["metadata"].get("user_id", 0))
        set_premium(user_id)
        return jsonify({"status": "premium_set"}), 200
    return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    app.run(debug=True)