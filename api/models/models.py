from api import db


class Cities(db.Model):

    __tablename__ = 'Cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('States.id'), nullable=False)


class States(db.Model):

    __tablename__ = 'States'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    short_name = db.Column(db.String(5), nullable=False)


class CEPS(db.Model):

    __tablename__ = 'CEPS'

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(30), nullable=True)
    logradouro = db.Column(db.String(500), nullable=False)
    nome_do_bairro = db.Column(db.String(500), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('States.id'), nullable=False)
