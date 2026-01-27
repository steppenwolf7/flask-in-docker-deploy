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
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: #000;
                color: #00ffcc;
                font-family: 'Arial', sans-serif;
                font-size: 3em;
                text-align: center;
            }
            img {
                margin-top: 30px;
                max-width: 90%;
                max-height: 65vh;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 255, 204, 0.5);
            }
            a {
                margin-top: 20px;
                color: #00ffcc;
                text-decoration: none;
                font-size: 0.5em;
                border: 2px solid #00ffcc;
                padding: 10px 20px;
                border-radius: 5px;
                transition: all 0.3s;
            }
            a:hover {
                background-color: #00ffcc;
                color: #000;
            }
        </style>
    </head>
    <body>
        <div>DecOps traning in progres ...</div>
        <img src="/static/diagram.png" alt="Architecture Diagram">
        <a href="https://github.com/steppenwolf7/flask-in-docker-deploy" target="_blank">
            📦 View on GitHub
        </a>
    </body>
    </html>
    """