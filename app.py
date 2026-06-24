from flask import Flask, request, jsonify, render_template
from detector import analyze_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing email text"}), 400

    result = analyze_email(data["text"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
