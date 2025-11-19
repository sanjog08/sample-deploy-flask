from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "your site is running 24/7"

