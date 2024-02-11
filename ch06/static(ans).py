from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

#----------practice start------------
@app.route('/test_static')
def test_static():
    print(app.url_map)
    html_str = f"""
    <!DOCTYPE html>
<html>
<head>
    <link rel="icon" href="{url_for('static', filename='img/favicon.ico')}">
    <title>Document</title>
</head>
<body>
    <h1>{url_for('static',filename="img/favicon.ico")}</h1>
</body>
</html>
"""
    return html_str
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
