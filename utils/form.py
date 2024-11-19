from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange


class OrcFormComum(FlaskForm):
    tamanho_01 = FloatField('Tamanho 1', validators=[
        DataRequired(message="Este campo é obrigatório"),
        NumberRange(min=0, message="Por favor, insira um número válido")
    ])
    tamanho_02 = FloatField('Tamanho 2', validators=[
        DataRequired(message="Este campo é obrigatório"),
        NumberRange(min=0, message="Por favor, insira um número válido")
    ])

    vidro = SelectField(
        choices=[('180.1', 'Fume de 4m'), ('130.0', 'Incolor de 3m'), ('150.0', 'Incolor de 4m'), ('230.0', 'Incolor de 6m'), ('180.3', 'Boreal de 4m'), ('180.2', 'Canelado de 4m'), ('200.0', 'Espelho de 4m')], validators=[DataRequired()]
    )

class OrcFormTemperado(FlaskForm):
    tamanho_01 = FloatField('Tamanho 1', validators=[
        DataRequired(message="Este campo é obrigatório"),
        NumberRange(min=0, message="Por favor, insira um número válido")
    ])
    tamanho_02 = FloatField('Tamanho 2', validators=[
        DataRequired(message="Este campo é obrigatório"),
        NumberRange(min=0, message="Por favor, insira um número válido")
    ])

    vidro = SelectField(
        choices=[('portaCorrer2v', 'Porta de Correr 2v'), ('portaCorrer4v', 'Porta de Correr 4v'), ('janela2v', 'Janela 2v'), ('janela4v', 'Janela 4v'), ('portaAbrir', 'Porta de abrir'), ('IncBascu', 'Inc Basculhante'), ('FumeBascu', 'Fume Basculhante'), ('box2v', 'Box 2v')], validators=[DataRequired()]
    )

class FormCliente(FlaskForm):
    nome = StringField(validators=[DataRequired()])
    numero = IntegerField(validators=[DataRequired()])
    preco = FloatField(validators=[DataRequired()])
    status = SelectField(choices=[
        ('pago', 'Pago'), ('npago', 'Não Pagou')
    ], validators=[DataRequired()])
    pedido = StringField(validators=[DataRequired()])
    # Tamanho 
    tamanho01 = FloatField(validators=[DataRequired()])
    tamanho02 = FloatField(validators=[DataRequired()])
    # Endereço
    end_bairro = StringField(validators=[DataRequired()])
    end_casa_numero = IntegerField(validators=[DataRequired()])
    end_adicional = StringField(validators=[DataRequired()])