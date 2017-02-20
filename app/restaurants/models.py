from app.database import db

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
