from flask import Flask
app = Flask(__name__)
from routes import * 

app.secret_key = "OPEN"

if __name__ == "__main__":
    app.run(debug=True, port=7500)