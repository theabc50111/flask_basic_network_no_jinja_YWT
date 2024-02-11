from flask import Flask, request

# practice start
from pathlib import Path
import uuid
# practice end

app = Flask(__name__)

# practice start
UPLOAD_FOLDER = Path(__file__).resolve().parent/'uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
# practice end

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# practice start
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == "GET":
        file_form_str = """
    <form method="POST" action="/upload_file" enctype="multipart/form-data">
        <label for="form_file_id">Select file</label>
        <input type="file" name="file" id="form_file_id">
        <input type="submit" value="submit">
    </form>"""
        return file_form_str
    elif request.method == "POST":
        file = request.files['file'] # key is the value of name(html attribute) in <input type="file">
        if file:
            filename = str(uuid.uuid4())+"_"+file.filename
            file.save(UPLOAD_FOLDER/filename)
        data = [["method:", request.method],
                ["base_url:", request.base_url],
                ["file:",file.filename]]
        table_str = ""
        print(data)
        for (name, content) in data:
            print(name, content)
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