import jwt
import threading
import logging
from datetime import datetime, timezone

from twilio.auth_strategy.auth_type import AuthType
from twilio.auth_strategy.auth_strategy import AuthStrategy
from twilio.http.token_manager import TokenManager


class TokenAuthStrategy(AuthStrategy):
    def __init__(self, token_manager: TokenManager):
        super().__init__(AuthType.ORGS_TOKEN)
        self.token_manager = token_manager
        self.token = None
        self.lock = threading.Lock()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_auth_string(self) -> str:
        pass

    def requires_authentication(self) -> bool:
        pass

    def fetch_token(self):
        pass

    def is_token_expired(self, token):
        pass
