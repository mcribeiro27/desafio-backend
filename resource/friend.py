from flask import Blueprint, request, jsonify
from models.friends_models import FriendModel
from flask_jwt_extended import jwt_required

friend = Blueprint('friend_routes', __name__, url_prefix = '/account')

''' Recupera todos os Friends'''


@friend.route('/friends')
@jwt_required
def get_all():
    return {'Friends': [friend.json() for friend in FriendModel.query.all()]}

''' Recupera Friend '''
@friend.route('/friend/<string:friend_id>')
@jwt_required
def get(friend_id):
    friend = FriendModel.find_friend(friend_id)
    if friend:
        return friend.json()
    return {'mensage': 'Friend não existe'}, 404 # Not Found

''' Salva Friend'''
@friend.route('/friend', methods=['POST'])
@jwt_required
def post():
    query = request.json
    friend = FriendModel(**query)
    if FriendModel.find_friend(query['friend_id']):
            return {"message":"Friend id '{}' already exists.".format(query['friend_id'])}, 400 # BAD REQUEST
    try:
        friend.save_friend()
        return {'mensage': 'Friend cadastrado com sucesso'}, 200 # OK
    except:
        return {'message': 'Internal Error'}, 500 # INTERNAL ERROR

    return friend.json()

''' Atualiza/Cadastra Friend'''
@friend.route('/friend/<string:friend_id>', methods=['PUT'])
@jwt_required
def put(friend_id):
    query = request.json
    friend_encontrado = FriendModel.find_friend(friend_id)

    # Caso exista um Friend, atualiza
    if friend_encontrado:
        friend_encontrado.update_friend(**query)
        try:
            friend_encontrado.save_friend()
        except:
            return {'message': 'Houve um erro interno no servidor ao Salvar um Friend'}, 500
        return friend_encontrado.json(), 200 # Success

    # Caso não exista, cria-se um Friend
    friend = FriendModel(friend_id, **query)
    try:
        friend.save_friend()
    except:
        return {'message': 'Houve um erro interno no servidor ao Salvar um Friend'}, 500 # INTERNAL ERROR
    
    return friend.json(), 201 # Created

''' Deleta Friend '''
@friend.route('/friend/<string:friend_id>', methods=['DELETE'])
@jwt_required
def delete(friend_id):
    friend = FriendModel.find_friend(friend_id)
    if friend:
        friend.delete_friend()
        return {'message': 'Friends deletado.'}
    return {'message': 'Friends não encontrado.'}, 404
