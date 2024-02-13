from flask import Flask, request

app = Flask(__name__)



@app.route('/')
def index():
    return "Hi"

@app.route("/req")
def req():
# ----------practice start------------
# ----------practice end--------------
    html_str =f"""
<table>
        {table_str}
</table>"""
    return html_str

if __name__ == '__main__':
    app.run(debug=True)


