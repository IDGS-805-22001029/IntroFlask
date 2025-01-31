from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo="Chi"
    lista=["Pedor","Juan","Pepe"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/user/<string:user>')
def user(user):
    return f"Hola, {user}"




@app.route('/user/<int:n>/<string:user>')
def username(id,username):
    return f"El usuario es : {username}, con el id: {id}"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return f'La suma es: {n1} + {n2}'

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label>nombre</label>
            </form>
            '''


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

if __name__ == '__main__':
    app.run(debug=True, port=3000)