import urllib.parse
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── ROUTES ──────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template(
        "index.html",
        supabase_url=os.getenv("SUPABASE_URL", "https://vhykbpifcwzxqgmlchrh.supabase.co"),
        supabase_key=os.getenv("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZoeWticGlmY3d6eHFnbWxjaHJoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU0NTM4MjIsImV4cCI6MjA5MTAyOTgyMn0.WDwaOhkfv8scRAUnUL9SGZ0ZnG1mFxtabs5RTqhJXZ8"),
    )


@app.route("/inquiry", methods=["POST"])
def inquiry():
    """Receives inquiry form data and returns a WhatsApp redirect URL."""
    data = request.get_json(silent=True) or {}

    # Sanitise inputs with length caps
    name    = str(data.get("name",    "Customer"))[:100]
    phone   = str(data.get("phone",   ""))[:20]
    event   = str(data.get("event",   ""))[:100]
    date    = str(data.get("date",    ""))[:50]
    budget  = str(data.get("budget",  ""))[:50]
    message = str(data.get("message", ""))[:500]

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

    wa_url = "https://wa.me/918238894242?text=" + urllib.parse.quote(text)
    return jsonify({"wa_url": wa_url})


# ── RUN ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV", "production") == "development"
    app.run(debug=debug_mode, host="0.0.0.0", port=5000)
