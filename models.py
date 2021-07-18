"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

#MODELS

DEFAULT_IMG_URL = 'https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMG_URL)

    #def image_url(self):
        #"""Returns image"""
        #return self.image or DEFAULT_IMG_URL

    def serialize(self):
        """Serialize cupcake to dict"""
        return {
            'id':self.id,
            'flavor':self.flavor,
            'rating':self.rating,
            'size':self.size,
            'image':self.image,
        }