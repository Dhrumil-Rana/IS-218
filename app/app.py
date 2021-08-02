import mysql.connector
from flaskext.mysql import MySQL
import simplejson as json
from flask import Flask, Response, request, redirect
from flask import render_template
from pymysql.cursors import DictCursor


app = Flask(__name__, template_folder="templates")
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'homework'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Dhrumil'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, people=result)


@app.route('/view/<int:person_Index>', methods=['GET'])
def record_view(person_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', person=result[0])


@app.route('/edit/<int:person_Index>', methods=['GET'])
def form_edit_get(person_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', person=result[0])


@app.route('/edit/<int:person_Index>', methods=['POST'])
def form_update_post(person_Index):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Height_Inches'), request.form.get('Weight_Pounds'), person_Index)
    print(inputData)
    sql_update_query = """UPDATE hw_200 t SET t.Height_Inches = %s, t.Weight_Pounds = %s WHERE t.Index = %s"""
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/people/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New person Form')


@app.route('/people/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Height_Inches'), request.form.get('Weight_Pounds'))
    sql_insert_query = """INSERT INTO hw_200 (Height_Inches, Weight_Pounds) VALUES (%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:person_Index>', methods=['POST'])
def form_delete_post(person_Index):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM hw_200 WHERE `Index` = %s """
    cursor.execute(sql_delete_query, person_Index)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/people', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/people/<int:person_Index>', methods=['GET'])
def api_retrieve(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/people/', methods=['POST'])
def api_add() -> str:
    content = request.json
    cursor = mysql.get_db().cursor()
    inputData = ( content['Height_Inches'], content['Weight_Pounds'] )
    sql_insert_query = """INSERT INTO hw_200 (Height_Inches,Weight_Pounds) VALUES (%s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/people/<int:person_Index>', methods=['PUT'])
def api_edit(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Height_Inches'], content['Weight_Pounds'], person_Index)
    sql_update_query = """UPDATE hw_200 t SET t.Height_Inches = %s, t.Weight_Pounds = %s WHERE t.`Index` = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/people/<int:person_Index>', methods=['DELETE'])
def api_delete(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM hw_200 WHERE `Index` = %s """
    cursor.execute(sql_delete_query, person_Index)
    mysql.get_db().commit()
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
