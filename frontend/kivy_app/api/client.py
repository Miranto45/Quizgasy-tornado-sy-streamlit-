
import json

from kivy.network.urlrequest import UrlRequest


class ApiClient:
    def __init__(self, base_url: str, on_error):
        self.base_url, self.on_error, self.token = base_url, on_error, ""

    def request(self, path, on_ok, body=None, on_fail=None):
        """GET si body est None, POST sinon. Les erreurs vont à on_error (popup) puis on_fail."""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        def failed(message):
            self.on_error(message)
            if on_fail:
                on_fail()

        UrlRequest(
            self.base_url + path,
            req_body=json.dumps(body) if body is not None else None,
            req_headers=headers,
            on_success=lambda req, res: on_ok(res),
            on_failure=lambda req, res: failed(self._detail(res)),
            on_error=lambda req, err: failed("Tsy afaka mifandray amin'ny serveur"),
        )

    @staticmethod
    def _detail(res) -> str:
        detail = res.get("detail") if isinstance(res, dict) else None
        return detail if isinstance(detail, str) else "Misy olana (hamarino ny fenoina)"
