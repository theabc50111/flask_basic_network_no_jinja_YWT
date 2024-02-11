from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"

@app.route("/req")
def req():
# ----------practice start------------
    data = [["args:", request.args],
           ["values:", request.values],
           ["cookies:", request.cookies],
           ["headers:", request.headers],
           ["host:", request.host],
           ["method:", request.method],
           ["path:", request.path],
           ["query_string:", request.query_string],
           ["full_path:", request.full_path],
           ["url:", request.url],
           ["base_url:", request.base_url],
           ["remote_addr:", request.remote_addr]]
    table_str = ""
    for (name, content) in data:
        table_str += f"""
        <tr style="border: 1px solid black">
            <td style="border: 1px solid black">
                {name}
            </td>
            <td style="border: 1px solid black">
                {content}
            </td>
        </tr>\n"""
# ----------practice end--------------
    html_str =f"""
<table>
        {table_str}
</table>"""
    return html_str


if __name__ == '__main__':
    app.run(debug=True)
