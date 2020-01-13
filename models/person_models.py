from sql_alchemy import lucree

class PersonModel(lucree.Model):
    __tablename__ = 'person'

    user_id = lucree.Column(lucree.String, primary_key=True)
    first_name = lucree.Column(lucree.String(10))
    last_name = lucree.Column(lucree.String(40))
    birthday = lucree.Column(lucree.String(11))
    password = lucree.Column(lucree.String(120))
    username = lucree.Column(lucree.String(10))
    friends = lucree.relationship('FriendModel')
    cards = lucree.relationship('CardModel')
    transfers = lucree.relationship('TransferModel')
    
    def __init__(self, user_id, first_name, last_name, birthday, password, username):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.password = password
        self.username = username

    def json(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'password': self.password,
            'username': self.username,
            'friends': [friend.json() for friend in self.friends],
            'cards': [card.json() for card in self.cards],
            'transfers': [transfer.json() for transfer in self.transfers]
        }
    
    ''' Busca na tabela Person'''
    @classmethod
    def find_person(cls, user_id):
        person = cls.query.filter_by(user_id=user_id).first()
        if person:
            return person
        return None

    ''' Salva na tabela Person'''
    def save_person(self):
        lucree.session.add(self)
        lucree.session.commit()

    ''' Atualiza a tabela Person'''
    def update_person(self, first_name, last_name, birthday, password, username):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.password = password
        self.username = username

    ''' Apaga na Tabela Person'''
    def delete_person(self):
        lucree.session.delete(self)
        lucree.session.commit()