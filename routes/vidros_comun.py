from flask import Blueprint, render_template, flash, request
from utils.form import OrcFormComum, OrcFormTemperado
import math

edit = Blueprint('vidros_comun', __name__)
valor_total = None
def calculo_temperado(nome_selecionado, med01,med02):
        global valor_total
        if nome_selecionado == "portaCorrer2v":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_aluminio = math.ceil(float(f"{med01*med02*105.0/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + valor_aluminio
            return valor_total

        elif nome_selecionado == "portaCorrer4v":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_aluminio = math.ceil(float(f"{med01*med02*105.0/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + valor_aluminio
            return valor_total

        elif nome_selecionado == "janela2v":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_aluminio = math.ceil(float(f"{med01*med02*105.0/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + valor_aluminio
            return valor_total
        
        elif nome_selecionado == "janela4v":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_aluminio = math.ceil(float(f"{med01*med02*105.0/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + valor_aluminio
            return valor_total
        
        elif nome_selecionado == "portaAbrir":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + 260
            return valor_total
        
        elif nome_selecionado == "IncBascu":
            valor_vidro = math.ceil(float(f"{med01*med02*190/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro
            return valor_total

        elif  nome_selecionado == "FumeBascu":
            valor_vidro = math.ceil(float(f"{med01*med02*210/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro
            return valor_total
        
        elif nome_selecionado == "Box 2v":
            valor_vidro = math.ceil(float(f"{med01*med02*350/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_aluminio = math.ceil(float(f"{med01*med02*105.0/10000:.3f}".replace('.', '.').replace(',', '.')))
            valor_total = valor_vidro + valor_aluminio
            return valor_total

@edit.route('/vidros_comun', methods=['POST', 'GET'])
def vidro_c():
    form = OrcFormComum()
    valor_total=None
    if request.method == 'POST':
        med01 = form.tamanho_01.data
        med02 = form.tamanho_02.data    
        valor = float(form.vidro.data)  
        valor_total = math.ceil(float(f"{med01*med02*valor/10000:.3f}".replace('.', '.').replace(',', '.')))

    return render_template('vidros_comun.html', form=form, total=valor_total)

@edit.route('/vidros_temperados', methods=['GET', 'POST'])
def vidro_t():
    form = OrcFormTemperado()
    global valor_total
    if form.validate_on_submit():
        med01 = form.tamanho_01.data + 10
        med02 = form.tamanho_02.data + 10

        valor_selecionado = form.vidro.data
        valor_total = calculo_temperado(valor_selecionado, med01, med02)

        # valor_total = valor_aluminio + valor_vidro

    return render_template('vidros_temper.html', form=form, total=valor_total)