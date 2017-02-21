from app.database import db

menu_cources = [
    {'id': 1, 'name': 'Starters'},
    {'id': 2, 'name': 'House specials'},
    {'id': 3, 'name': 'Meal deals'},
    {'id': 4, 'name': 'Drinks and desserts'},
]

class Restaurant(db.Model):
    """Registered user capable of viewing and editing.
    
    :param str name: name of the resurant
    :param str image: url of the resurant image
    :param str description: the resturant description

    """
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64))
    description = db.Column(db.String(64), nullable=False)


class MenuItem(db.Model):

    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.String(8))
    course = db.Column(db.Integer)
    description = db.Column(db.String(64), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship(Restaurant)
    

