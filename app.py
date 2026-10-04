from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Studio 6IX</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                background: #080808;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .hero {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 30px;
                box-sizing: border-box;
            }

            .content {
                max-width: 700px;
            }

            .logo {
                color: #d4af37;
                letter-spacing: 6px;
                font-size: 14px;
                font-weight: bold;
            }

            h1 {
                font-size: clamp(48px, 12vw, 100px);
                margin: 25px 0 10px;
                letter-spacing: -3px;
            }

            p {
                color: #aaa;
                font-size: 18px;
                line-height: 1.6;
            }

            .button {
                display: inline-block;
                margin-top: 30px;
                padding: 16px 30px;
                background: #d4af37;
                color: #080808;
                text-decoration: none;
                font-weight: bold;
                letter-spacing: 2px;
            }
        </style>
    </head>

    <body>
        <section class="hero">
            <div class="content">

                <div class="logo">
                    STUDIO 6IX
                </div>

                <h1>
                    YOUR NEXT CUT.
                </h1>

                <p>
                    A premium barber booking platform
                    built for modern barbers and their clients.
                </p>

                <a class="button" href="#">
                    BOOK YOUR CHAIR
                </a>

            </div>
        </section>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()