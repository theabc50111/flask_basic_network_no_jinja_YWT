#----------practice start------------

#----------practice end--------------


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/user/<name>')
def user(name):
    return f"<h1> Hi! {name}"

#----------practice start------------

#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)