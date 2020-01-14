from flask import Blueprint, request
from models.person_models import PersonModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

person = Blueprint('person_routes', __name__, url_prefix = '/account')

''' Recupera todos os Persons'''
@person.route('/persons')
def get_all():
    return {'Persons': [person.json() for person in PersonModel.query.all()]}


''' Recupera Person '''
@person.route('/person/<string:user_id>')
def get(user_id):
    user = PersonModel.find_person(user_id)
    if user:
        return user.json()
    return {'mensage': 'Person não existe'}, 404 # Not Found


''' Cadatra Person'''
@person.route('/person', methods=['POST'])
def post():
    query = request.json
    user = PersonModel(**query)
    if PersonModel.find_person(query['user_id']):
            return {"message":"Person id '{}' already exists.".format(query['user_id'])}, 400 # BAD REQUEST
    try:
        user.save_person()
        return {'mensage': 'Usuario cadastrado com sucesso'}, 200 # OK
    except:
        return {'message': 'Internal Error'}, 500 # INTERNAL ERROR

    return user.json()

''' Atualiza/Cadatra Person'''

@person.route('/person/<string:user_id>', methods=['PUT'])
@jwt_required
def put(user_id):
    query = request.json
    user_encontrado = PersonModel.find_person(user_id)

    # Caso exista um Person, atualiza
    if user_encontrado:
        user_encontrado.update_person(**query)
        try:
            user_encontrado.save_person()
        except:
            return {'message': 'Houve um erro interno no servidor ao Salvar o person'}, 500
        return user_encontrado.json(), 200 # Success

    # Caso não exista, cria-se um Person
    person = PersonModel(user_id, **query)
    
    try:
        person.save_person()
    except:
        return {'message': 'Houve um erro interno no servidor ao Salvar o Person'}, 500 # INTERNAL ERROR
    
    return person.json(), 201 # Created

''' Deleta Person'''

@person.route('/person/<string:user_id>', methods=['DELETE'])
@jwt_required
def delete(user_id):
    person = PersonModel.find_person(user_id)
    if person:
        person.delete_person()
        return {'message': 'Person deletado.'}
    return {'message': 'Person não encontrado.'}, 404


@person.route('/login', methods=['POST'])
def login():
    query = request.json
    user = PersonModel.find_by_username(query['username'])

    if user and safe_str_cmp(user.password, query['password']):
        token_de_acesso = create_access_token(identity=user.user_id)
        return {'access_token': token_de_acesso}, 200
    return {'message': 'Username or password not found'}, 401


@person.route('/logout', methods=['POST'])
@jwt_required
def logout():
    jwt_id = get_raw_jwt()['jti']
    BLACKLIST.add(jwt_id)
    return {'message': 'Deslogado com sucesso'}, 200