"""Construction de l'application Tornado."""
import tornado.web

import settings
from routes import ROUTES


def make_app() -> tornado.web.Application:
    return tornado.web.Application(ROUTES, static_path=str(settings.STATIC_DIR), static_url_prefix="/static/")
