from flask import Blueprint, request
from models.person_models import PersonModel

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
def delete(user_id):
    person = PersonModel.find_person(user_id)
    if person:
        person.delete_person()
        return {'message': 'Person deletado.'}
    return {'message': 'Person não encontrado.'}, 404
