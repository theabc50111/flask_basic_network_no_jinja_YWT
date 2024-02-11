from flask import Flask, request, send_from_directory
from pathlib import Path

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# practice start
@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    if request.method == "GET":
        file_name_form_str = """
    <form method="POST" action="/download_file">
        <label for="file_name_id">File name</label>
        <input type="text" name="file_name" id="file_name_id" >
        <input type="submit" value="submit">
    </form>"""
        return file_name_form_str
    elif request.method == "POST":
        file_name = request.form['file_name']
        file_dir = Path(__file__).resolve().parent/'uploaded'
    return send_from_directory(file_dir, file_name, as_attachment=True)
# practice end

if __name__ == "__main__":
    app.run(debug=True)