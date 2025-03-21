from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session 
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_livre/<int:livre_id>')
def Readfiche(livre_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE id = ?', (livre_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')</ndef ReadBDD():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']

    # Connexion à la base de données
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau livre
    cursor.execute('INSERT INTO livres (created, titre, auteur, disponible) VALUES (?, ?, ?, ?)', (1002938, titre, auteur, 1))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                                                      
if __name__ == "__main__":
  app.run(debug=True)
