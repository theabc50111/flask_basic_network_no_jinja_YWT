from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# practice start
@app.route('/form')
def get_form():
    form_str = """
<form method="POST" action="/form_result">
    <label for="demo_input_text_id">Input account</label>
    <input type="text" name="account" id="demo_input_text_id">
    <label for="demo_input_password_id">Input password</label>
    <input type="password" name="passwords" id="demo_input_password_id">
    <input type="submit" value="submit">
</form>"""

    return form_str

@app.route('/form_result', methods=['POST']) # default methods is "GET"
def form_result():
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
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
    html_str =f"""
<table>
        {table_str}
</table>"""
    return html_str
# practice end


if __name__ == "__main__":
    app.run(debug=True)
