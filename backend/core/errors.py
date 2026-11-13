"""Erreur métier : chaque framework la convertit en réponse HTTP."""


class CoreError(Exception):
    def __init__(self, status: int, detail: str):
        super().__init__(detail)
        self.status, self.detail = status, detail
