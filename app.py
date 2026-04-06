from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# ── ROUTES ──────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inquiry", methods=["POST"])
def inquiry():
    """Receives the inquiry form and returns a WhatsApp redirect URL."""
    data = request.get_json(silent=True) or {}
    name    = data.get("name", "Customer")
    phone   = data.get("phone", "")
    event   = data.get("event", "")
    date    = data.get("date", "")
    budget  = data.get("budget", "")
    message = data.get("message", "")

    text = (
        f"Hi The Surprise Events! 🎊\n\n"
        f"Name: {name}\n"
        f"Phone: {phone}\n"
        f"Event: {event}\n"
        f"Date: {date}\n"
        f"Budget: {budget}\n"
        f"\nMessage: {message}\n\n"
        f"I'd like to inquire about decoration for my event. Please get in touch!"
    )

    import urllib.parse
    wa_url = "https://wa.me/918238894242?text=" + urllib.parse.quote(text)
    return jsonify({"wa_url": wa_url})


# ── RUN ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
