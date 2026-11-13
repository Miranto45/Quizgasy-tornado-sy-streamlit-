from core.config import DEFAULT_QUIZ_SIZE
from core.errors import CoreError
from core.services import quiz_service
from realtime.hub import hub
from .base import ApiHandler


class Questions(ApiHandler):
    def get(self):
        if not self.auth_user():
            return
        try:
            n = int(self.get_argument("n", str(DEFAULT_QUIZ_SIZE)))
        except ValueError:
            return self.fail(422, "n tsy marina")
        self.write_list(quiz_service.public_questions(n))


class Submit(ApiHandler):
    async def post(self):
        user = self.auth_user()
        if not user:
            return
        try:
            self.write(quiz_service.submit(user["id"], self.json_body().get("answers")))
        except CoreError as e:
            return self.fail(e.status, e.detail)
        await hub.refresh()  # le classement live se met à jour tout de suite
