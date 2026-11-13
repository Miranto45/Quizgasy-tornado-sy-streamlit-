# core - logique partagée (pas un serveur)
```
core/
├── __init__.py        crée la base au premier import
├── config.py          chemin de la base, limites (nom, mot de passe, taille du quiz)
├── errors.py          CoreError(status, detail)
├── database.py        connexion SQLite + schéma
├── data/
│   └── questions.py   les 20 questions en malagasy
└── services/
    ├── auth_service.py    register, login, user_for_token
    ├── quiz_service.py    public_questions, submit (score côté serveur)
    └── stats_service.py   leaderboard, me
```
Les deux backends ne contiennent que la couche web : ils appellent ces services.
