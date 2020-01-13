from flask import Blueprint, request,json
from models.transfers_model import TransferModel
from models.friends_models import FriendModel
from models.cards_models import CardModel

transfer = Blueprint('transfer_routes', __name__, url_prefix = '/account')

@transfer.route('/bank_statement')
def get_all():
    return {'Transfers': [transfer.json() for transfer in TransferModel.query.all()]}

@transfer.route('/bank_statement/<string:person_id>')
def get(person_id):
    person = TransferModel.find_person(person_id)
    if person:
        return {'transfer':[transfer.json() for transfer in TransferModel.query.filter(TransferModel.person_id == person_id).all()]}
    return {'mensage': 'Person não existe'}, 404 # Not Found

@transfer.route('/transfer', methods=['POST'])
def post():
    query = request.json
    transfer = TransferModel(query['friend_id'], query['total_to_pay'], query['billing_card']['card_id'], query['person_id'])
    billing = dict(query['billing_card'])
    if not FriendModel.find_friend(query['friend_id']):
        return {'message': 'Friend Not Found'}, 404
    elif not CardModel.find_card(billing['card_id']):
        return {'message': 'Card Not Found'}, 404

    try:
        transfer.save_transfer()
        return {'mensage': 'Transfer realizada com sucesso'}, 200 # OK 
    
    except:
        return {'message': 'Internal Error'}, 500 # INTERNAL ERROR 
