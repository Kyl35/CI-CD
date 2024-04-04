Ce projet consiste à créer un prototype d'un logiciel tout en respectant les bonnes pratiques du devops. Le code nous est déjà fourni, nous l'avons donc intégré dans le projet.

1. Création du dépôt sur GitHub
- Créez un nouveau dépôt sur GitHub.
- Clonez le dépôt sur votre PC en utilisant la commande `git clone <url_du_depot>`.

2. Création du projet Flask
- Créez un projet Flask.
- Si ce n'est pas fait, installez Flask en exécutant `pip install Flask` et insérez-y le code fourni.

 3. Création d'une Azure Web App
- Créez une Azure Web App pour héberger l'application Flask.
- Configurez les paramètres concernant l'hébergement de l'application ; les variables d'environnement, les autorisations d'accès, etc.

 4. Récupération du Azure Profile
- Récupérez le profil de publication Azure de votre Web App.
- Utilisez vos identifiants pour accéder au profil de publication.

5. Création de la pipeline CI/CD sur GitHub Actions
- Créez un fichier de configuration (par exemple `.github/workflows/main_devopscdci.yml`) dans votre dépôt.
- Configurez les jobs et les étapes de la pipeline pour le build, les tests et le déploiement de l'application.

6. Tests de la pipeline
- Effectuez des modification dans votre code et poussez-les (push) vers votre dépôt.
- Suivez l'exécution de la pipeline CI/CD dans l'onglet Actions de votre dépôt.
- Consultez les logs et les résultats des étapes de la pipeline pour vous assurer du déroulement correct du processus.
- Vérifiez que l'application est déployée avec succès sur votre Azure Web App et qu'elle fonctionne.
