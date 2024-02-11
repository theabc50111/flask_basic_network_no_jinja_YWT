#----------practice start------------
from flask import Flask, url_for
#----------practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/user/<name>')
def user(name):
    return f"<h1> Hi! {name}"

#----------practice start------------
@app.route('/url_for')
def test_urlfor():
    print(app.url_map)
    html_str = """   
{url_for('index')}
<hr>
{url_for('user',name='user1')}
<hr>
{url_for('user',name='abc',page=10)}
<hr>
{url_for('test_urlfor')}
<hr>
{url_for('test_urlfor',_external=True)}
<hr>
{url_for('test_urlfor', name='john', page=2, version=1)}
<hr>
{url_for('test_urlfor',_external=True, name='john', page=2, version=1}}"""
    return html_str
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
