from flask import Flask, request, send_from_directory
from pathlib import Path

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# practice start
# practice end

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
