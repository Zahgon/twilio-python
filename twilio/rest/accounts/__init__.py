from warnings import warn

from twilio.rest.accounts.AccountsBase import AccountsBase
from twilio.rest.accounts.v1.auth_token_promotion import AuthTokenPromotionList
from twilio.rest.accounts.v1.credential import CredentialList
from twilio.rest.accounts.v1.secondary_auth_token import SecondaryAuthTokenList


class Accounts(AccountsBase):
    @property
    def auth_token_promotion(self) -> AuthTokenPromotionList:
        pass

    @property
    def credentials(self) -> CredentialList:
        pass

    @property
    def secondary_auth_token(self) -> SecondaryAuthTokenList:
        pass
