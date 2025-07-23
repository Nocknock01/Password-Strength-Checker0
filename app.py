from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Function to evaluate password strength
def password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count how many conditions are True
    score = sum([
        bool(length),
        bool(digit),
        bool(upper),
        bool(lower),
        bool(special)
    ])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Route to load the HTML page
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle password strength checking
@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.get_json()
        password = data.get("password", "")
        strength = password_strength(password)
        return jsonify({"strength": strength})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
