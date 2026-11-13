# backend
```
backend/
├── core/          logique partagée : base SQLite, questions, services (auth, quiz, stats)
├── fastapi_app/   FastAPI :8000  - routers/, schemas.py, dependencies.py
└── tornado_app/   Tornado :8001  - handlers/, realtime/, static/ (+ API identique)
```
Même contrat d'API des deux côtés ; seul le framework change. Voir le README de chaque dossier.
