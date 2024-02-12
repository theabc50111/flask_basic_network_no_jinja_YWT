# --------------Practice start--------------
# --------------Practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# --------------Practice start--------------
# --------------Practice end--------------

if __name__ == '__main__':
    app.run(debug=True)