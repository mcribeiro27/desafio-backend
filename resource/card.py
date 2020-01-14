from flask import Blueprint, request
from models.cards_models import CardModel
from flask_jwt_extended import jwt_required

card = Blueprint('card_routes', __name__, url_prefix = '/account')

''' Recupera todos os Cards'''
@card.route('/cards')
@jwt_required
def get_all():
    return {'Cards': [card.json() for card in CardModel.query.all()]}


''' Recupera Card '''
@card.route('/card/<string:card_id>')
@jwt_required
def get(card_id):
    card = CardModel.find_card(card_id)
    if card:
        return card.json()
    return {'mensage': 'Card não existe'}, 404 # Not Found


''' Cadastra Card '''
@card.route('/card', methods=['POST'])
@jwt_required
def post():
    query = request.json
    card = CardModel(**query)
    if CardModel.find_card(query['card_id']):
            return {"message":"Card id '{}' already exists.".format(query['card_id'])}, 400 # BAD REQUEST
    try:
        card.save_card()
        return {'mensage': 'Card cadastrado com sucesso'}, 200 # OK
    except:
        return {'message': 'Internal Error'}, 500 # INTERNAL ERROR

    return card.json()

''' Atualiza/Cadastra Card'''
@card.route('/card/<string:card_id>', methods=['PUT'])
@jwt_required
def put(card_id):
    query = request.json
    card_encontrado = CardModel.find_card(card_id)

    # Caso exista um Card, atualiza
    if card_encontrado:
        card_encontrado.update_card(**query)
        try:
            card_encontrado.save_card()
        except:
            return {'message': 'Houve um erro interno no servidor ao Salvar o Card'}, 500
        return card_encontrado.json(), 200 # Success

    # Caso não exista, cria-se um Card
    card = CardModel(card_id, **query)
    
    try:
        card.save_card()
    except:
        return {'message': 'Houve um erro interno no servidor ao Salvar o Card'}, 500 # INTERNAL ERROR
    
    return card.json(), 201 # Created

''' Deleta Card'''
@card.route('/card/<string:card_id>', methods=['DELETE'])
@jwt_required
def delete(card_id):
    card = CardModel.find_card(card_id)
    if card:
        card.delete_card()
        return {'message': 'Card deletado.'}
    return {'message': 'Card não encontrado.'}, 404
