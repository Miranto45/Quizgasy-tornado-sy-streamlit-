# frontend
```
frontend/
├── kivy_app/        app Android/desktop : screens/, kv/, api/, services/
└── streamlit_app/   client web : views/, components/, state.py, api_client.py
```
Les deux clients parlent la même API et marchent avec FastAPI (:8000) comme avec Tornado (:8001).
