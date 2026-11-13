# fastapi_app - FastAPI (port 8000)
```
fastapi_app/
├── main.py            création de l'app, gestion d'erreurs, inclusion des routers
├── schemas.py         modèles Pydantic
├── dependencies.py    current_user (jeton Bearer)
└── routers/
    ├── auth.py        POST /register, POST /login
    ├── quiz.py        GET /questions, POST /submit
    └── stats.py       GET /leaderboard, GET /me
```
```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000   # docs : http://localhost:8000/docs
```
