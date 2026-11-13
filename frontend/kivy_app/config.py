
# PC (desktop)                    -> "127.0.0.1"
# Émulateur Android               -> "10.0.2.2"
# Vrai téléphone (même Wi-Fi)     -> IP du PC, ex. "192.168.1.10"
HOST = "127.0.0.1"
API_PORT = 8000   # 8000 = backend FastAPI, 8001 = backend Tornado (même API)
WS_PORT = 8001    # Tornado : classement en direct (repli HTTP si arrêté)
API = f"http://{HOST}:{API_PORT}"
WS = f"ws://{HOST}:{WS_PORT}/ws"
QUIZ_SIZE = 10
