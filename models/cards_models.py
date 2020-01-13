from sql_alchemy import lucree

class CardModel(lucree.Model):
    __tablename__ = 'card'

    card_id = lucree.Column(lucree.String(120), primary_key=True)
    title = lucree.Column(lucree.String(40))
    pan = lucree.Column(lucree.String(40))
    expiry_mm = lucree.Column(lucree.String(2))
    expiry_yyy = lucree.Column(lucree.String(4))
    security_code = lucree.Column(lucree.String(3))
    date = lucree.Column(lucree.String(11))
    person_id = lucree.Column(lucree.String, lucree.ForeignKey('person.user_id'))
 

    def __init__(self, card_id, title, pan, expiry_mm, expiry_yyy, security_code, date, person_id):
        self.card_id = card_id
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyy = expiry_yyy
        self.security_code = security_code
        self.date = date
        self.person_id = person_id

    def json(self):
        return {
            'card_id': self.card_id,
            'title': self.title,
            'pan': self.pan,
            'expiry_mm': self.expiry_mm,
            'expiry_yyy': self.expiry_yyy,
            'security_code': self.security_code,
            'date': self.date,
            'person_id': self.person_id
        }

    ''' Busca na tabela Cards'''
    @classmethod
    def find_card(cls, card_id):
        card = cls.query.filter_by(card_id=card_id).first()
        if card:
            return card
        return None

    ''' Salva na tabela Card '''
    def save_card(self):
        lucree.session.add(self)
        lucree.session.commit()

    ''' Atualiza a tabela Card '''
    def update_card(self, title, pan, expiry_mm, expiry_yyy, security_code, date):
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyy = expiry_yyy
        self.security_code = security_code
        self.date = date

    ''' Apaga na Tabela Card '''
    def delete_card(self):
        lucree.session.delete(self)
        lucree.session.commit()