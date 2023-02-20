from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import AddPetForm,EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'thebestsecretkey'

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Pet adoption homepage"""
    pets = Pet.query.all()

    return render_template("homepage.html",pets=pets)

@app.route('/add',methods=["POST","GET"])
def add_pet_form():
    """Add pet form and handler"""
    
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("pet_add_form.html",form=form)

@app.route('/<int:qid>',methods=["POST","GET"])
def pet_info_page(qid):
    """Pet info page"""
    
    pet = Pet.query.get_or_404(qid)
    
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.add(pet)
        db.session.commit()

        return redirect(f"/{qid}")

    return render_template("pet_info.html",pet=pet,form=form)

