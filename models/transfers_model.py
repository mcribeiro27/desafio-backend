from sql_alchemy import lucree
from models.cards_models import CardModel
from datetime import datetime
from flask import jsonify

class TransferModel(lucree.Model):
    __tablename = 'transfer'
    now = datetime.now()

    transfer_id = lucree.Column(lucree.Integer, primary_key=True)
    friend_id = lucree.Column(lucree.String, lucree.ForeignKey('friends.friend_id'))
    person_id = lucree.Column(lucree.String, lucree.ForeignKey('person.user_id'))
    total_to_pay = lucree.Column(lucree.Integer)
    billing_card = lucree.Column(lucree.String)
    date = lucree.Column(lucree.DateTime, nullable=False,
        default=datetime.utcnow)

    def __init__(self, friend_id, total_to_pay, billing_card, person_id):
        self.friend_id = friend_id
        self.total_to_pay = total_to_pay
        self.billing_card = billing_card
        self.person_id = person_id

        
    def json(self):
        return {
            'friend_id': self.friend_id,
            'person_id': self.person_id,
            'total_to_pay': self.total_to_pay,
            'from_card': self.billing_card, 
            'date': self.date
        }

    @classmethod
    def find_transfer(cls, transfer_id):
        transfer = cls.query.filter_by(transfer_id=transfer_id).first()
        if transfer:
            return transfer
        return None

    @classmethod
    def find_person(cls, person_id):
        person = cls.query.filter_by(person_id=person_id).first()
        print(person)
        if person:
            return person
        return None


    def save_transfer(self):
        lucree.session.add(self)
        lucree.session.commit()
