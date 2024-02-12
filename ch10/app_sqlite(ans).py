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
    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 5

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_customers)
    proxy = connection.execute(query)

    # fetch data & decided by page
    query = db.select(table_customers).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()

    # Close connection
    connection.close()
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
    if request.method=="POST":
        try:
            connection  = engine.connect()
            query = db.select(func.max(table_customers.c.CustomerId)).order_by(table_customers.c.CustomerId)
            proxy = connection.execute(query)
            max_id = proxy.fetchall()[0][0]
            print(type(max_id), max_id)
            print(request.form)
            print(request.form['CustomerId'])
            if int(request.form['CustomerId']) <= max_id:
                query = db.update(table_customers).where(table_customers.c.CustomerId == request.form['CustomerId']).values(**request.form)
                connection.execute(query)
                connection.commit()
            else:
                raise Exception # 輸入的CustomerId 不可以大於
        except:
            req_form = request.form.copy()
            req_form.update({"update_db": False})
            res = req_form
            return jsonify(res)
        else:
            req_form = request.form.copy()
            req_form.update({"update_db": True})
            res = req_form
            return jsonify(res)
        finally:
            # Close connection
            connection.close()
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
