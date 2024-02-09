CREATE TABLE classe_devops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    notes FLOAT,
    autre_colonne VARCHAR(255)
);

INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom1', 'Prénom1', 15.5);
INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom2', 'Prénom2', 14.0);
INSERT INTO classe_devops (nom, prenom, notes) VALUES ('Nom3', 'Prénom3', 12.5);
-- Ajoutez autant d'insertions que nécessaire pour remplir votre table

