from twilio.rest.preview_iam.PreviewIamBase import PreviewIamBase

from twilio.rest.preview_iam.v1.authorize import (
    AuthorizeList,
)
from twilio.rest.preview_iam.v1.token import (
    TokenList,
)
from twilio.rest.preview_iam.versionless.organization import (
    OrganizationList,
)
from twilio.rest.preview_iam.versionless import Versionless


class PreviewIam(PreviewIamBase):
    @property
    def organization(self) -> OrganizationList:
        pass

    @property
    def authorize(self) -> AuthorizeList:
        pass

    @property
    def token(self) -> TokenList:
        pass
