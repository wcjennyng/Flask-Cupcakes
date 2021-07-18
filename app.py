"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """Homepage"""
    
    return render_template('index.html')

@app.route('/api/cupcakes')
def all_cupcakes():
    """Data about all cupcakes"""
    """Respond with JSON like: 
    {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):  
    """Returns data about a single cupcake"""
    """Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Creates a cupcake with flavor, size, rating, image"""
    """Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}"""
    data=request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Update cupcake with the id passed in URL. Return updated data"""
    """Respond with JSON of the newly-updated cupcake, like this: {cupcake: {id, flavor, size, rating, image}}"""

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete cupcake with id passed in the URL. 
    Respond with JSON like {message: "Deleted"}
    Should raise a 404 if the cupcake cannot be found"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(message="Deleted!")    