from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(160), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    # Tamanho
    tamanho01 = db.Column(db.Float, nullable=False)
    tamanho02 = db.Column(db.Float, nullable=False)
    # Endereço
    end_bairro = db.Column(db.String(250), nullable=False)
    end_casa_numero = db.Column(db.Integer, nullable=False)
    end_adicional = db.Column(db.String(250), nullable=False)
    pedido = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Cliente ID={self.id}, Nome={self.nome}, Preço={self.preco}>"

class VendaPorMes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(250), nullable=True)
    valor = db.Column(db.Float, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
