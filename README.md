# BOOK API VERSION 1

## Getting Started

### Installation des Dépendances

#### Python 3.10.0
#### pip 21.3.1 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl http://localhost:5000/livres
```
       {
    "livres": [
        {
            "auteur": "bernard dae",
            "categorie_id": 2,
            "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT",
            "editeur": "ste",
            "id": 3,
            "isnb": "paoo",
            "titre": "pagneir"
        },
        {
            "auteur": "bere",
            "categorie_id": 2,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "se",
            "id": 4,
            "isnb": "pabi",
            "titre": "per"
        },
        {
            "auteur": "bernakkre",
            "categorie_id": 3,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "stlle",
            "id": 5,
            "isnb": "pavb",
            "titre": "pagnvver"
        },
        {
            "auteur": "bernakkrett",
            "categorie_id": 3,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "stllett",
            "id": 6,
            "isnb": "pavvvb",
            "titre": "pagnvvert"
        },
        {
            "auteur": "bernakrrkrett",
            "categorie_id": 4,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "stllerrtt",
            "id": 7,
            "isnb": "pavvvrb",
            "titre": "pagnvrrvert"
        },
        {
            "auteur": "berett",
            "categorie_id": 4,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "stllerrtfft",
            "id": 8,
            "isnb": "parb",
            "titre": "pagvert"
        },
        {
            "auteur": "berkrpppett",
            "categorie_id": 5,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "stptt",
            "id": 10,
            "isnb": "pmbbgb",
            "titre": "parkkt"
        },
        {
            "auteur": "TUNDE",
            "categorie_id": 6,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "BELAC",
            "id": 11,
            "isnb": "pmyhb",
            "titre": "phhart"
        }
    ],
    "success": true,
    "total": 8
}
```

.##GET/livres(livre_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/livres/3
```
   {
    "livres": {
        "auteur": "bernard dae",
        "categorie_id": 2,
        "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT",
        "editeur": "ste",
        "id": 3,
        "isnb": "paoo",
        "titre": "pagneir"
    },
```


. ## DELETE/livres (livre_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/livre/1
```
    {
        "id_livre": 1,
        "new_total": 3,
        "success": true
    }
```

. ##PATCH/livres(livre_id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/livres/1 -H "Content-Type:application/json" -d '{"auteur": "Azychika, Takumi Fukui","editeur": "Ki-oon","titre": "Jujutsu Kaisen"}'
  ```
  ```
    {
        "auteur": "Azychika, Takumi Fukui",
        "code_ISBN": "979-1-0327",
        "date_publication": "03-02-2022",
        "editeur": "Ki-oon",
        "id": 1,
        "titre": "Jujutsu Kaisen"
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

        {
    "categories": [
        {
            "id": 1,
            "libelle_categorie": "action"
        },
        {
            "id": 3,
            "libelle_categorie": "fixion"
        },
        {
            "id": 4,
            "libelle_categorie": "harlequin"
        },
        {
            "id": 5,
            "libelle_categorie": "sup"
        },
        {
            "id": 6,
            "libelle_categorie": "sup1"
        },
        {
            "id": 2,
            "libelle_categorie": "amourr"
        },
        {
            "id": 7,
            "libelle_categorie": "bb"
        },
        {
            "id": 8,
            "libelle_categorie": "kcksb"
        },
        {
            "id": 9,
            "libelle_categorie": "kBb"
        }
    ],
    "success": true,
    "total": 9
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/2
```
   {
    "categories": {
        "id": 2,
        "libelle_categorie": "amourr"
    },
    "selected_id": 2,
    "succes": true
}
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/9
```
    {



    }
```

. ##PATCH/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/4' -H "Content-Type:application/json" -d '{"categorie": "Bandes Dessinées"}'
  ```
  ```
    {
        "categorie": "Bandes Dessinées",
        "id": 4
    }

.##GET/categories/(categorie_id)/livres
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: http://localhost:5000/categories/2/livres
```
    {
    "Nombre de livre de la categorie": 2,
    "livres": [
        {
            "auteur": "bernard dae",
            "categorie_id": 2,
            "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT",
            "editeur": "ste",
            "id": 3,
            "isnb": "paoo",
            "titre": "pagneir"
        },
        {
            "auteur": "bere",
            "categorie_id": 2,
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "se",
            "id": 4,
            "isnb": "pabi",
            "titre": "per"
        }
    ],
    "success": true
}
```

