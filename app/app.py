from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL



app = Flask(__name__)

#CONECTION MYSQL
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root@1234"
app.config["MYSQL_DB"]="abaco"

conexion = MySQL(app)



@app.before_request
def before_request():
    print("Before the request ....")

@app.after_request
def after_request(response):
    print("After the request ....")
    return response

@app.route('/')
def index():
    
    courses = ["PHP","PYTHON","JAVA","JAVASCRIPT","KOTLIN"]
    data={
        "title":"Index123",
        "welcome":"Saludos",
        "courses": courses,
        "number_of_courses": len(courses)
    }
    return render_template('index.html', data=data)
#dynamic url <>
@app.route("/contact/<name>/<int:age>")
def contact(name,age):
    data={
        "title":"Contact",
        "name":name,
        "age":age}
    return render_template('contact.html', data=data)

#http://127.0.0.1:5000/query_string?param1=example
def query_string():
    print(request)
    print(request.args)
    print(request.args.get("param1"))
    print(request.args.get("param2"))
    return "OK"

@app.route("/cursos")
def listar_cursos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT codigo, nombre, credito FROM curso ORDER BY nombre ASC"
        cursor.execute(sql) 
        cursos= cursor.fetchall()
        print(cursos)
        data["mensaje"] = "Exito"
        data["cursos"] = cursos   
    except Exception as ex:
        data["mensaje"] = ex
    return jsonify(data)
#manitodice usar fetchone no fetchall



def page_not_found(error):
    # return render_template("404.html"), 404
    return redirect(url_for("index"))



if __name__ =='__main__':
    app.add_url_rule("/query_string", view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug = True, port = 5000)