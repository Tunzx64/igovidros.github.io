from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Clientes, VendaPorMes, db
from datetime import datetime, timedelta

home = Blueprint('home', __name__)
anotacoes = []

@home.route('/about')
def about():
    return render_template('about.html')

@home.route('/')
def index():
    clientes = Clientes.query.all()
    data_limite = datetime.now() - timedelta(days=30)
    registros_antigos = VendaPorMes.query.filter(VendaPorMes.data_criacao < data_limite).all()
    
    if registros_antigos:
        for registro in registros_antigos:
            db.session.delete(registro)        
        db.session.commit()
        flash(f'{len(registros_antigos)} registros antigos foram removidos com sucesso!', 'success')
    else:
        flash('Vendas Carregadas Seja Bem vindo.', 'info')

    return render_template('base.html', anot=anotacoes, pedidos=clientes)

@home.route('/api/anote', methods=['GET', 'POST'])
def anote():
    print("Requisição recebida")  # Para verificar se a função é chamada
    global anotacoes
    if request.method == 'POST':
        nova_anotacao = request.form.get('anotae')
        if nova_anotacao:
            anotacoes.append(nova_anotacao)
            print(f"Anotação adicionada: {nova_anotacao}")
        else:
            print("Nenhuma anotação foi recebida.")

        return redirect(url_for('home.index'))
    return render_template('base.html')

@home.route('/api/limp_anote', methods=['GET', 'POST'])
def limp_anote():
    global anotacoes
    if request.method == 'POST':
        if anotacoes:
            anotacoes.pop()
            flash('Anotações limpas !')
        else:
            flash('Não tem nenhuma anotação !')
    
    return redirect(url_for('home.index'))
