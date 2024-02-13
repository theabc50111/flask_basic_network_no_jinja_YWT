from flask import Flask, request, jsonify
import sqlalchemy as db
from sqlalchemy import func

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# sql setting
path_to_db = "./db/chinook.db"
table = 'customers'
engine = db.create_engine(f'sqlite:///{path_to_db}')
metadata = db.MetaData()
table_customers = db.Table(table, metadata, autoload_with=engine)



@app.route('/data-list')
def data_list():
    # --------------Practice start--------------
    # --------------Practice end--------------
    th_str = ""
    for col_key in table_customers.columns.keys():
        th_str += f"""
            <th style="border: 1px solid black">
                {col_key}
            </th>\n"""
    thead_str = f"""
    <thead>
        <tr>
        {th_str}
        </tr>
    </thead>
    """
    tbody_str = ""
    for each_customer in results:
        td_str = ""
        for col in each_customer:
            td_str += f"""
                <td style="border: 1px solid black">
                    {col}
                </td>\n"""
        tbody_str += f"""
            <tr style="border: 1px solid black">
            {td_str}
            </tr>\n"""
    html_str =f"""
<table>
        {thead_str}
        {tbody_str}
</table>"""
    return html_str

@app.route('/data-edit', methods=["GET", "POST"])
def data_edit():
    # --------------Practice start--------------
    # --------------Practice end--------------
    if request.method=="GET":
        form_str = """
<form method="POST" action="/data-edit">
    <label for="custormer_id_input_id">Input customer ID</label>
    <input type="text" name="CustomerId" id="custormer_id_input_id">
    <label for="first_name_input_id">Input customer First Name</label>
    <input type="text" name="FirstName" id="first_name_input_id">
    <label for="last_name_input_id">Input customer Last Name</label>
    <input type="text" name="LastName" id="last_name_input_id">
    <input type="submit" value="submit">
</form>"""

    return form_str

if __name__ == "__main__":
    app.run(debug=True)
