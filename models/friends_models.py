from sql_alchemy import lucree

class FriendModel(lucree.Model):
    __tablename__ = 'friends'

    friend_id = lucree.Column(lucree.String(120), primary_key=True)
    first_name = lucree.Column(lucree.String(10))
    last_name = lucree.Column(lucree.String(40))
    birthday = lucree.Column(lucree.String(11))
    username = lucree.Column(lucree.String(10))
    person_id = lucree.Column(lucree.String, lucree.ForeignKey('person.user_id'))
    transfer = lucree.relationship('TransferModel')
    
    def __init__(self, friend_id, first_name, last_name, birthday, username, person_id):
        self.friend_id = friend_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.person_id = person_id

    def json(self):
        return {
            'friend_id': self.friend_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'username': self.username,
            'person_id': self.person_id
        }

    ''' Busca na tabela Friends'''
    @classmethod
    def find_friend(cls, friend_id):
        friend = cls.query.filter_by(friend_id=friend_id).first()
        if friend:
            return friend
        return None

    ''' Salva na tabela Friend'''
    def save_friend(self):
        lucree.session.add(self)
        lucree.session.commit()

    ''' Atualiza a tabela Friend'''
    def update_friend(self, first_name, last_name, birthday, username, person_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.person_id = person_id

    ''' Apaga na Tabela Person'''
    def delete_friend(self):
        lucree.session.delete(self)
        lucree.session.commit()