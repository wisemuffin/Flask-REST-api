from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # lazy=dynamic means self.items is now a query builder rather than an object. Creating objects for each item would be too expenseive!
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        # same as "SELECT * FROM items WHERE name=name LIMIT 1" and dont need to define connection or cursor
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)  # session is a collection of objects we are going to write to the db
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
