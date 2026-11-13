# tornado_app - Tornado (port 8001)
Même API que FastAPI + WebSocket `/ws` + page live sur `/`.
```
tornado_app/
├── server.py          point d'entrée (boucle asyncio, relecture périodique)
├── application.py     make_app()
├── settings.py        port, dossier static, période de relecture
├── routes.py          table des URL
├── handlers/
│   ├── base.py        ApiHandler : erreurs JSON, corps JSON, authentification
│   ├── auth.py        Register, Login
│   ├── quiz.py        Questions, Submit
│   ├── stats.py       Leaderboard, Me
│   ├── pages.py       Index (page live), Health
│   └── live.py        LiveWS (WebSocket)
├── realtime/
│   └── hub.py         LiveHub : clients connectés + diffusion du classement
└── static/
    ├── live.html
    ├── css/live.css
    └── js/live.js
```
```bash
pip install -r requirements.txt
python server.py
```
