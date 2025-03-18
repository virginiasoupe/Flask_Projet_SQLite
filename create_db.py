import sqlite3

connection = sqlite3.connect('bibliotheque.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Ajout d'utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", ('DUPONT', 'Emilie', 'emilie.dupont@email.com', 'hashed_password1', 'user'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", ('LEROUX', 'Lucas', 'lucas.leroux@email.com', 'hashed_password2', 'user'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", ('MARTIN', 'Amandine', 'amandine.martin@email.com', 'hashed_password3', 'admin'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", ('TREMBLAY', 'Antoine', 'antoine.tremblay@email.com', 'hashed_password4', 'user'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", ('LAMBERT', 'Sarah', 'sarah.lambert@email.com', 'hashed_password5', 'admin'))

# Ajout de livres
cur.execute("INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1))
cur.execute("INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, ?)", ('1984', 'George Orwell', 1))
cur.execute("INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, ?)", ('L’Étranger', 'Albert Camus', 1))
cur.execute("INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, ?)", ('Les Misérables', 'Victor Hugo', 1))
cur.execute("INSERT INTO livres (titre, auteur, disponible) VALUES (?, ?, ?)", ('Harry Potter à l'école des sorciers', 'J.K. Rowling', 1))

connection.commit()
connection.close()
