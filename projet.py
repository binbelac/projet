
from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
app = Flask(__name__)

motdepasse=quote_plus('caleb')
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:caleb@localhost:5432/base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db=SQLAlchemy(app)


#creation des tables

@app.after_request
def after_request(reponse):
    reponse.headers.add('Acces-Control-Allow-Headers',
                        'Content-Type,Authorization,true')
    reponse.headers.add('Access-Control-Allow-Methods',
                        'GET,PUT,POST,DELETE,OPTIONS,PATCH')
    return reponse


class Categories(db.Model):
    __tablename__='Categories'
    id=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(50),nullable=False)
    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie
  
    def insert(self): 
        db.session.add(self)
        db.session.commit()

    def update(self):
       db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return{
            'id':self.id,
            'libelle_categorie':self.libelle_categorie
        }


class Livres(db.Model):
    __tablename__='Livres'
    id=db.Column(db.Integer,primary_key=True)
    isnb=db.Column(db.String(15),unique=True,nullable=False)
    titre=db.Column(db.String(50),nullable=False)
    date_publication=db.Column(db.Date,nullable=False)
    auteur=db.Column(db.String(20),nullable=False)
    editeur=db.Column(db.String(25),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey(Categories.id))
    def __init__(self,isnb,titre,date_publication,auteur,editeur,categorie_id):
        self.isnb=isnb
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id

    def insert(self): 
        db.session.add(self)
        db.session.commit()

    def update(self):
       db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return{
            'id':self.id,
            'isnb':self.isnb,
            'titre':self.titre,
            'date_publication':self.date_publication,
            'auteur':self.auteur,
            'editeur':self.editeur,
            'categorie_id':self.categorie_id
        }

db.create_all()




####################################################################
#
#      Endpoint liste de tous les livres
#
#####################################################################
@app.route('/livres')
def get_all_livres():
    book=Livres.query.all()
    formated_book=[et.format() for et in book]
    return jsonify({
      'success':True,  
      'total':len(book),
      "livres" : formated_book
    })



####################################################################
#
#      Endpoint chercher un livre par son id
#
#####################################################################
@app.route('/livres/<int:id>')
def selectionner_livre(id):
    livres=Livres.query.get(id)
    if livres is None:
        abort(404)
    else:
        return jsonify({
             'succes':True,
            'selected_id':id,
            'livres':livres.format()
        })


####################################################################
#
#      Endpoint supprimer un livre
#
#####################################################################
@app.route('/livres/<int:id>',methods=['DELETE'])   
def delete_livre(id):
    livres=Livres.query.get(id)
    if livres is None:
        abort(404)
    else:
        livres.delete()
        return jsonify({ 
            'succes':True,
            'id':id,
            'livres':livres.format(),
            'total_livres':Livres.query.count()

        })

####################################################################
#
#      Endpoint Modifier les informations d’un livre
#
#####################################################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def modifier_livres(id):
    body=request.get_json()
    livres=Livres.query.get(id)  
    if livres is None:
        abort(404)
    else:
     livres.isnb=body.get('isnb')  
     livres.titre=body.get('titre')
     livres.date_publication=body.get('date_publication')
     livres.auteur=body.get('auteur')
     livres.editeur=body.get('editeur')
     livres.update()
     return jsonify({
         'success':True,
         'update_id':id,
         'livres':livres.format(),
     })


####################################################################
#
#      Endpoint Listes toutes les catégories
#
#####################################################################
@app.route('/categories')
def get_all_cat():
    cat=Categories.query.all()
    cat=[et.format() for et in cat]
    return jsonify({
      'success':True,  
      'total':len(cat),
      'categories' : cat
    })  

####################################################################
#
#      Endpoint Chercher une catégorie par son id
#
#####################################################################   
@app.route('/categories/<int:id>')
def selectionner_cat(id):
    categories=Categories.query.get(id)
    if categories is None:
        abort(404)
    else:
        return jsonify({
             'succes':True,
            'selected_id':id,
            'categories':categories.format()
        })


####################################################################
#
#      Endpoint Modifier categories
#
#####################################################################
@app.route('/categories/<int:id>',methods=['PATCH'])
def modifier_cat(id):
    body=request.get_json()
    categories=Categories.query.get(id)  
    if categories is None:
        abort(404)
    else:
     categories.libelle_categorie=body.get('libelle_categorie') 
     categories.update() 
     return jsonify({
         'success':True,
         'update_id':id,
         'categories':categories.format()
     })

####################################################################
#
#      Endpoint supprimer categories
#
#####################################################################
app.route('/categories/<int:id>',methods=['DELETE'])  
def delete_cat(id):
    try:

        cat=Categories.query.get(id)
        cat.delete(id)    
        return jsonify({ 
                'succes':True,
                'id':id,
                'categorie':cat.format(),
                'total_categorie':Categories.query.count()
        }) 
    except:
        abort(404)
    finally:
        db.session.close()



####################################################################
#
#   LISTER LES LIVRES D'UNEE CATEGORIE
#
#####################################################################

@app.route('/categories/<int:id>/livres')
def get_liv_cat(id):
    x=Livres.query.filter(Livres.categorie_id==id).all()
    try:
        e=0
        return jsonify({
            'success':True,
            'livres':[l.format() for l in x],
            'Nombre de livres par categorie':len(x)
        })
    except:
        abort(400)
        


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "succes":False,
        "error":404,
        "message":"not found"
    })

@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "succes":False,
        "error":404,
        "message":"bad request"
    })


