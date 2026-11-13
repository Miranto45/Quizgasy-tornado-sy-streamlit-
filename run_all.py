
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CMDS = [
    ([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"], "backend/fastapi_app"),
    ([sys.executable, "server.py"], "backend/tornado_app"),
    ([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501"], "frontend/streamlit_app"),
]
procs = [subprocess.Popen(cmd, cwd=ROOT / folder) for cmd, folder in CMDS]
print("FastAPI :8000/docs | Tornado :8001 | Streamlit :8501")
try:
    for p in procs:
        p.wait()
except KeyboardInterrupt:
    for p in procs:
        p.terminate()
