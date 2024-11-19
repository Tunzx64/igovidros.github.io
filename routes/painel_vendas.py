from flask import Blueprint, render_template, url_for, redirect, flash, request
from models import Clientes, VendaPorMes, db
from utils.form import FormCliente

vendas = Blueprint('venda', __name__)

@vendas.route('/agendar_pedido', methods=['POST', 'GET'])
def fazer_uma_venda():
    form = FormCliente()
    if form.validate_on_submit():
        nome = form.nome.data
        numero = form.numero.data
        pedido = form.pedido.data
        preco = form.preco.data
        status = form.status.data

        med01 = form.tamanho01.data
        med02 = form.tamanho02.data

        bairro = form.end_bairro.data
        casa_numero = form.end_casa_numero.data
        adicional = form.end_adicional.data

        if Clientes.query.filter_by(nome=nome).first():
            flash('Já existe um cliente com esse nome cadastrado !')
            return redirect(url_for('venda.fazer_uma_venda'))
        
        pedido_cliente = Clientes(nome=nome, numero=numero, pedido=pedido, end_bairro=bairro, end_casa_numero=casa_numero, end_adicional=adicional, status=status, tamanho01=med01, tamanho02=med02, preco=preco)
        
        db.session.add(pedido_cliente)
        db.session.commit()
        flash('Pedido agendado com sucesso !')
        return redirect(url_for('venda.painel_de_venda'))
    return render_template('agendar_pedido.html', form=form)

@vendas.route('/painel_vendas', methods=['GET', 'POST'])
def painel_de_venda():
    clientes = Clientes.query.all()
    form = FormCliente()
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)

    # Filtragem e Paginação
    pedidos_query = Clientes.query
    if search_query:
        pedidos_query = pedidos_query.filter(Clientes.nome.ilike(f"%{search_query}%"))  
    pedidos_paginated = pedidos_query.paginate(page=page, per_page=6)  # 6 por página

    return render_template('vendas.html', form=form, client=clientes,  pedidos=pedidos_paginated)

@vendas.route('/edit_product/<int:client_id>', methods=['POST', 'GET'])
def editar_produto(client_id):
    print('Entrei no função')
    client = Clientes.query.get_or_404(client_id)
    form = FormCliente(obj=client)
    print(client)
    print(form)
    if form.validate_on_submit():
        nome = form.nome.data
        if Clientes.query.filter(Clientes.nome == nome, Clientes.id != client_id).first():
            flash('Já tem um produto com esse nome !')
            return redirect(url_for('venda.painel_de_venda'))
        print('Entrei no form validate')
        client.nome = form.nome.data
        client.numero = form.numero.data
        client.pedido = form.pedido.data
        client.preco = form.preco.data
        client.status = form.status.data

        client.med01 = form.tamanho01.data
        client.med02 = form.tamanho02.data

        client.bairro = form.end_bairro.data
        client.casa_numero = form.end_casa_numero.data
        client.adicional = form.end_adicional.data

        try:
            print('Entrei no salvamento')
            db.session.commit()
            flash('Pedido atualizdo com sucesso !')
            return redirect(url_for('venda.painel_de_venda'))
        except Exception as e:
            print('Entrei no except')
            db.session.rollback()
            flash(f'Ocorreu um erro {e}')
            return redirect(url_for('venda.painel_de_venda'))

    print('Redirecionando !')
    return redirect(url_for('venda.painel_de_venda'))

@vendas.route('/remove_pedido/<int:client_id>', methods=['GET', 'POST'])
def finalizar_pedido(client_id):
    # Busca o cliente pelo ID
    cliente = Clientes.query.get(client_id)

    if cliente:
        try:
            # Cria um registro de vendas baseado no cliente
            venda = VendaPorMes(nome=cliente.nome, valor=cliente.preco)
            db.session.add(venda)
            
            # Exclui o cliente do banco
            db.session.delete(cliente)
            
            # Salva as alterações no banco
            db.session.commit()

            flash('Pedido Finalizado com sucesso!')
        except Exception as e:
            # Trata erros ao interagir com o banco de dados
            db.session.rollback()
            flash(f'Ocorreu um erro ao finalizar o pedido: {str(e)}')
    else:
        flash('Nenhum pedido encontrado!')

    # Redireciona para a tela principal
    return redirect(url_for('venda.painel_de_venda'))


@vendas.route('/relatorio_vendas', methods=['GET', 'POST'])
def relatorios_de_vendas():
    vendas = VendaPorMes.query.all()
    total_vendas = sum(venda.valor for venda in vendas) 
    return render_template('vendas_finalizadas.html', pedidos_vendidos=vendas, total=total_vendas)
