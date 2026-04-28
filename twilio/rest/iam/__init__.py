from warnings import warn

from twilio.rest.iam.IamBase import IamBase
from twilio.rest.iam.v1.api_key import ApiKeyList
from twilio.rest.iam.v1.get_api_keys import GetApiKeysList


class Iam(IamBase):
    @property
    def api_key(self) -> ApiKeyList:
        pass

    @property
    def get_api_keys(self) -> GetApiKeysList:
        pass
