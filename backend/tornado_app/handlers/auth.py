from core.errors import CoreError
from core.services import auth_service
from .base import ApiHandler


class Register(ApiHandler):
    def post(self):
        b = self.json_body()
        try:
            self.write(auth_service.register(b.get("username"), b.get("password")))
        except CoreError as e:
            self.fail(e.status, e.detail)


class Login(ApiHandler):
    def post(self):
        b = self.json_body()
        try:
            self.write(auth_service.login(b.get("username"), b.get("password")))
        except CoreError as e:
            self.fail(e.status, e.detail)
