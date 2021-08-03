from werkzeug.security import generate_password_hash
from flask import render_template, url_for, Blueprint
import mysql.connector
import simplejson as json
from flask import Response, request, redirect
from .forms import ContactForm, SignupForm
from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL

mysql = MySQL(cursorclass=DictCursor)
views = Blueprint('routes', __name__)

@views.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template("contact.jinja2", form=form, template="form-template")


@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.jinja2",
        form=form,
        template="form-template",
        title="Signup Form"
    )

@views.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template(
        "success.jinja2",
        template="success-template"
    )

@views.route('/', methods=['GET'])
def index():
    user = {'username': 'Dhrumil'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, people=result)


@views.route('/view/<int:person_Index>', methods=['GET'])
def record_view(person_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', person=result[0])


@views.route('/edit/<int:person_Index>', methods=['GET'])
def form_edit_get(person_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', person=result[0])


@views.route('/edit/<int:person_Index>', methods=['POST'])
def form_update_post(person_Index):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Height_Inches'), request.form.get('Weight_Pounds'), person_Index)
    print(inputData)
    sql_update_query = """UPDATE hw_200 t SET t.Height_Inches = %s, t.Weight_Pounds = %s WHERE t.Index = %s"""
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@views.route('/people/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New person Form')


@views.route('/people/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Height_Inches'), request.form.get('Weight_Pounds'))
    sql_insert_query = """INSERT INTO hw_200 (Height_Inches, Weight_Pounds) VALUES (%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@views.route('/delete/<int:person_Index>', methods=['POST'])
def form_delete_post(person_Index):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM hw_200 WHERE `Index` = %s """
    cursor.execute(sql_delete_query, person_Index)
    mysql.get_db().commit()
    return redirect("/", code=302)


@views.route('/api/v1/people', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@views.route('/api/v1/people/<int:person_Index>', methods=['GET'])
def api_retrieve(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw_200 WHERE `Index`=%s', person_Index)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@views.route('/api/v1/people/', methods=['POST'])
def api_add() -> str:
    content = request.json
    cursor = mysql.get_db().cursor()
    inputData = ( content['Height_Inches'], content['Weight_Pounds'] )
    sql_insert_query = """INSERT INTO hw_200 (Height_Inches,Weight_Pounds) VALUES (%s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@views.route('/api/v1/people/<int:person_Index>', methods=['PUT'])
def api_edit(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Height_Inches'], content['Weight_Pounds'], person_Index)
    sql_update_query = """UPDATE hw_200 t SET t.Height_Inches = %s, t.Weight_Pounds = %s WHERE t.`Index` = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@views.route('/api/people/<int:person_Index>', methods=['DELETE'])
def api_delete(person_Index) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM hw_200 WHERE `Index` = %s """
    cursor.execute(sql_delete_query, person_Index)
    mysql.get_db().commit()
    resp = Response(status=210, mimetype='application/json')
    return resp

