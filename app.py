from flask import Flask, jsonify
from resource.person import person
from resource.friend import friend
from resource.card import card
from resource.transfer import transfer
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app = Flask(__name__)
app.register_blueprint(person)
app.register_blueprint(friend)
app.register_blueprint(card)
app.register_blueprint(transfer)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lucree.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'NaoRevelePraNinguem'
app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    lucree.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'Você já está deslogado'}), 401

@app.route('/')
def index():
    return jsonify({'message': 'Hello World'})

if __name__ == '__main__':
    from sql_alchemy import lucree
    lucree.init_app(app)
    app.run(debug=True)