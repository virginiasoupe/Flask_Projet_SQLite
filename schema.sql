DROP TABLE IF EXISTS livres;
DROP TABLE IF EXISTS utilisateurs;
DROP TABLE IF EXISTS emprunts;

CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    disponible INTEGER DEFAULT 1  -- 1 = disponible, 0 = emprunté
);

CREATE TABLE utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('admin', 'user'))  -- Gestion des rôles
);

CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur_id INTEGER NOT NULL,
    livre_id INTEGER NOT NULL,
    date_emprunt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_retour TIMESTAMP,
    retourne INTEGER DEFAULT 0,  -- 0 = pas encore retourné, 1 = retourné
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id),
    FOREIGN KEY (livre_id) REFERENCES livres(id)
);
