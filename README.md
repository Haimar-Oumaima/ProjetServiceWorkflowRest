# Guide d'installation et de déploiement de l'application

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Python 3
- Node.js
- Docker
- Docker Compose

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Haimar-Oumaima/ProjetServiceWorkflowRest.git
   ```

2. Accédez au répertoire de l'application :

   ```bash
   cd ProjetServiceWorkflowRest
   ```

3. Créez et activez un environnement virtuel Python :

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Sur Windows : venv\Scripts\activate
   ```

4. Installez les dépendances Python :

   ```bash
   pip install -r requirements.txt
   ```

5. Installez les dépendances JavaScript :

   ```bash
   npm install
   ```

## Configuration de la base de données

1. Assurez-vous que Docker est en cours d'exécution sur votre système.

2. Lancez MySQL dans un conteneur Docker en exécutant la commande suivante à la racine du projet :

   ```bash
   docker-compose up -d
   ```

3. La base de données MySQL sera accessible à l'adresse suivante : `mysql://user:password@localhost:3306/loan`.

## Lancement de l'application

1. Démarrez le serveur FastAPI avec Uvicorn :

   ```bash
   python3 -m uvicorn main:app --reload
   ```

2. Démarrez le serveur de développement frontend :

   ```bash
   npm run dev
   ```

3. Accédez à l'application dans votre navigateur à l'adresse suivante : [http://localhost:3000](http://localhost:3000)

