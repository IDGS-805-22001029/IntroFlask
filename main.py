from flask import Flask, render_template, request
from cine import cliente
import forms
from forms import ZodiacoForm
from datetime import datetime 


app = Flask(__name__)

app.secret_key='1234'

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

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/OperasBas", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        op = request.form.get("op")
        while True:
            if op == "+":
                resultado = "La suma de {} + {} = {}".format(n1,n2,str(int(n1)+int(n2)))
                return resultado
            elif op == "-":
                resultado = "La resta de {} - {} = {}".format(n1,n2,str(int(n1)-int(n2)))
                return resultado
            elif op == "/":
                resultado = "La división de {} / {} = {}".format(n1,n2,str(int(n1)/int(n2)))
                return resultado
            elif op == "*":
                resultado = "La multiplicación de {} * {} = {}".format(n1,n2,str(int(n1)*int(n2)))
                return render_template("OperasBas.html", resultado=resultado, n1=n1, n2=n2)

@app.route("/cineco", methods=["GET","POST"])
def cineco():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidad_p = int(request.form.get("cantidad_p"))
        cantidad_b = int(request.form.get("cantidad_b"))
        tarjeta_si = request.form.get("tarjeta_si")
        tarjeta_no = request.form.get("tarjeta_no")
        
        tarjeta = "si" if tarjeta_si == "true" else "no"
        
        total = cantidad_b * 12
        obj = cliente(nombre, cantidad_p, cantidad_b, tarjeta, total)
        
        if not obj.calculo_B(cantidad_b, cantidad_p):
            error = "La cantidad de boletos no puede ser mayor a 7 por persona"
            return render_template("cineco.html", error=error)
        
        obj.calculoD2(obj)
        obj.calculoD1(obj)
        obj.calculoD3(obj)
        
        valor = obj.total
        
        return render_template("cineco.html", valor=valor)
    
    return render_template("cineco.html")

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    matr=''
    nom = ''
    ape=''
    email=''
    alumno_clase = forms.UseForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        matr = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
    return render_template("alumnos.html", form= alumno_clase, matr=matr, nom=nom, ape=ape, email=email)


@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    hoy = datetime.today()
    nom = ''
    dia = 0
    mes = 0
    ano = 0
    edad = 0
    signo = ''
    signos = ["Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
    
    zodiaco_clase = ZodiacoForm(request.form)
    
    if request.method == "POST" and zodiaco_clase.validate():
        nom = zodiaco_clase.nom.data + " " + zodiaco_clase.apM.data + " " + zodiaco_clase.apP.data
        dia = zodiaco_clase.dia.data
        mes = zodiaco_clase.mes.data
        ano = zodiaco_clase.ano.data
        
        birthdate = datetime(ano, mes, dia)
        edad = hoy.year - birthdate.year - ((hoy.month, hoy.day) < (birthdate.month, birthdate.day))
        signo = signos[(ano - 1900) % 12]
    
    print(f"Nombre: {nom}, Edad: {edad}, Signo: {signo}")  # Depuraciónj
    return render_template("zodiaco.html", form=zodiaco_clase, nom=nom, signo=signo, edad=edad)

if __name__ == "__main__":
    app.run(debug=True)