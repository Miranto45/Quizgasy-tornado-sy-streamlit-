from core.services import stats_service
from .base import ApiHandler


class Leaderboard(ApiHandler):
    def get(self):
        if self.auth_user():
            self.write_list(stats_service.leaderboard())


class Me(ApiHandler):
    def get(self):
        user = self.auth_user()
        if user:
            self.write(stats_service.me(user))
