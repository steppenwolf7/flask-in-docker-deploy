from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Flask in Docker</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #000;
                color: #00ffcc;
                font-family: 'Arial', sans-serif;
                font-size: 3em;
                text-align: center;
            }
        </style>
    </head>
    <body>
        DecOps traning in progres ...
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
