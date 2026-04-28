from warnings import warn

from twilio.rest.content.ContentBase import ContentBase
from twilio.rest.content.v1.content import ContentList
from twilio.rest.content.v1.content_and_approvals import ContentAndApprovalsList
from twilio.rest.content.v1.legacy_content import LegacyContentList


class Content(ContentBase):
    @property
    def contents(self) -> ContentList:
        pass

    @property
    def content_and_approvals(self) -> ContentAndApprovalsList:
        pass

    @property
    def legacy_contents(self) -> LegacyContentList:
        pass
