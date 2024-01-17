# SIMPLON DEV IA | Brief 5

## Développer une API REST pour exposer un modèle prédictif avec des données immobilières

### Prérequis

Avant de démarrer le développement le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r ressources/requirements.txt
```

### Data

[Lien vers les données à utiliser](https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data)

### Notes

Tous les chemins sont absolus, utiliser des chemins relatifs me provoquait quelques erreurs, bien penser à tous les modifier sur votre environnement.

### Procédure

1 / Télécharger le fichier transactions.npz sur kaggle (voir data) <br><br>
2 / Convertir le fichier en .npz en .csv avec le script npz_to_csv.py (dossier /ressources) <br><br>
3 / Préparer les données pour les modèles avec data_process.py <br><br>
4 / (Optionnel) Tester les modèles avec model_testing.py <br><br>
5 / Entraîner et exporter les modèles avec model_training.py <br><br>
6 / Après avoir modifié les chemins des .pkl dans main.py, lancer le serveur local avec la commande suivante :
```bash
uvicorn main:app --reload
```

### Doc

Pour un hôte (127.0.0.1) et un port (8000), accédez à http://127.0.0.1:8000/docs sur votre navigateur, une fois le serveur lancé, pour accéder aux fonctionnalités de l'API.
