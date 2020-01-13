from flask import Flask, jsonify
from resource.person import person
from resource.friend import friend
from resource.card import card
from resource.transfer import transfer


app = Flask(__name__)
app.register_blueprint(person)
app.register_blueprint(friend)
app.register_blueprint(card)
app.register_blueprint(transfer)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lucree.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def cria_banco():
    lucree.create_all()

@app.route('/')
def index():
    return jsonify({'message': 'Hello World'})

if __name__ == '__main__':
    from sql_alchemy import lucree
    lucree.init_app(app)
    app.run(debug=True)