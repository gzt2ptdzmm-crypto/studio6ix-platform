from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Studio 6IX</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                background: #080808;
                color: white;
                font-family: Arial, sans-serif;
            }

            .container {
                max-width: 900px;
                margin: auto;
                padding: 60px 20px;
                text-align: center;
            }

            h1 {
                font-size: 55px;
                letter-spacing: 6px;
                margin-bottom: 10px;
            }

            .gold {
                color: #d4af37;
            }

            p {
                color: #aaa;
                font-size: 18px;
            }

            .button {
                display: inline-block;
                margin-top: 30px;
                padding: 16px 35px;
                background: #d4af37;
                color: #000;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
            }

            .button:hover {
                background: #f0cf55;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>STUDIO <span class="gold">6IX</span></h1>

            <p>
                Premium grooming. Modern style. Toronto.
            </p>

            <a class="button" href="/book">
                BOOK YOUR APPOINTMENT
            </a>

        </div>

    </body>
    </html>
    """


# =========================
# BOOKING PAGE
# =========================

@app.route("/book", methods=["GET", "POST"])
def book():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        service = request.form.get("service", "").strip()
        date = request.form.get("date", "").strip()
        time = request.form.get("time", "").strip()

        if not name or not phone or not service or not date or not time:
            return """
            <h2>Missing information</h2>
            <p>Please fill in all required fields.</p>
            <a href="/book">Go back</a>
            """, 400

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Booking Confirmed</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <style>
                body {{
                    background: #080808;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 70px 20px;
                }}

                h1 {{
                    color: #d4af37;
                }}

                .box {{
                    max-width: 500px;
                    margin: auto;
                    padding: 35px;
                    border: 1px solid #333;
                    border-radius: 10px;
                }}

                a {{
                    display: inline-block;
                    margin-top: 25px;
                    color: #d4af37;
                }}
            </style>
        </head>

        <body>

            <div class="box">

                <h1>BOOKING RECEIVED</h1>

                <p>Thank you, {name}.</p>

                <p>
                    <strong>{service}</strong>
                </p>

                <p>
                    {date} at {time}
                </p>

                <p>
                    We will confirm your appointment shortly.
                </p>

                <a href="/">Back to Studio 6IX</a>

            </div>

        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Book | Studio 6IX</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                background: #080808;
                color: white;
                font-family: Arial, sans-serif;
            }

            .container {
                max-width: 600px;
                margin: auto;
                padding: 40px 20px;
            }

            h1 {
                text-align: center;
                color: #d4af37;
                letter-spacing: 3px;
            }

            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
                margin-top: 30px;
            }

            input,
            select {
                padding: 15px;
                background: #151515;
                color: white;
                border: 1px solid #333;
                border-radius: 5px;
                font-size: 16px;
            }

            button {
                padding: 16px;
                background: #d4af37;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
            }

            button:hover {
                background: #f0cf55;
            }

            .back {
                display: block;
                text-align: center;
                margin-top: 25px;
                color: #d4af37;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>BOOK YOUR CHAIR</h1>

            <form method="POST" action="/book">

                <input
                    type="text"
                    name="name"
                    placeholder="Full Name"
                    required
                >

                <input
                    type="tel"
                    name="phone"
                    placeholder="Phone Number"
                    required
                >

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                >

                <select name="service" required>

                    <option value="">Select Service</option>

                    <option value="Signature Haircut">
                        Signature Haircut
                    </option>

                    <option value="Haircut + Beard">
                        Haircut + Beard
                    </option>

                    <option value="Beard Trim">
                        Beard Trim
                    </option>

                    <option value="Kids Haircut">
                        Kids Haircut
                    </option>

                </select>

                <input
                    type="date"
                    name="date"
                    required
                >

                <input
                    type="time"
                    name="time"
                    required
                >

                <button type="submit">
                    CONFIRM BOOKING
                </button>

            </form>

            <a class="back" href="/">
                ← Back to Studio 6IX
            </a>

        </div>

    </body>
    </html>
    """


# =========================
# API TEST ROUTE
# =========================

@app.route("/api/slots")
def slots():
    return jsonify({
        "success": True,
        "message": "Studio 6IX booking API is working.",
        "slots": [
            "09:30",
            "10:30",
            "11:30",
            "12:30",
            "13:30",
            "14:30",
            "15:30",
            "16:30",
            "17:30",
            "18:30",
            "19:30",
            "20:30"
        ]
    })


# =========================
# HEALTH CHECK
# =========================

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "app": "Studio 6IX"
    })


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )