from wtforms import Form
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, DateField
from wtforms import validators
from flask_wtf import FlaskForm

    

class UseForm(Form):

    matricula = StringField("Matricula", [validators.DataRequired(message = "Campo requerido"),
                                           validators.Length(min=3, max=10, message="La matricula debe tener 10 caracteres")])	
    nombre = StringField("Nombre", [validators.DataRequired(message = "Campo requerido"),
                                           validators.Length(min=3, max=10, message="La matricula debe tener 10 caracteres")])	
    apellido = StringField("Apellido", [validators.DataRequired(message = "Campo requerido"),
                                           validators.Length(min=3, max=10, message="La matricula debe tener 10 caracteres")])	
    email = StringField("Email", [validators.DataRequired(message = "Campo requerido"),
                                           validators.Length(min=10, max=20, message="La matricula debe tener 10 caracteres")])	
    

class ZodiacoForm(FlaskForm):
    sexo = RadioField("Sexo", choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], validators=[validators.DataRequired(message="Campo requerido")])
    dia = IntegerField("Dia", [validators.DataRequired(message="Campo requerido"), validators.NumberRange(min=1, max=31, message="El día debe estar entre 1 y 31")])
    mes = IntegerField("Mes", [validators.DataRequired(message="Campo requerido"), validators.NumberRange(min=1, max=12, message="El mes debe estar entre 1 y 12")])
    ano = IntegerField("Año", [validators.DataRequired(message="Campo requerido"), validators.NumberRange(min=1900, max=2023, message="El año debe estar entre 1900 y 2023")])
    nom = StringField("Nombre", [validators.DataRequired(message="Campo requerido"), validators.Length(min=3, max=15, message="El nombre debe tener entre 3 y 15 caracteres")])
    apM = StringField("Apellido Materno", [validators.DataRequired(message="Campo requerido"), validators.Length(min=3, max=15, message="El apellido materno debe tener entre 3 y 15 caracteres")])
    apP = StringField("Apellido Paterno", [validators.DataRequired(message="Campo requerido"), validators.Length(min=3, max=15, message="El apellido paterno debe tener entre 3 y 15 caracteres")])
    submit = SubmitField('Calcular')