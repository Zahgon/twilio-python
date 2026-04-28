from warnings import warn

from twilio.rest.verify.VerifyBase import VerifyBase
from twilio.rest.verify.v2.form import FormList
from twilio.rest.verify.v2.safelist import SafelistList
from twilio.rest.verify.v2.service import ServiceList
from twilio.rest.verify.v2.template import TemplateList
from twilio.rest.verify.v2.verification_attempt import VerificationAttemptList
from twilio.rest.verify.v2.verification_attempts_summary import (
    VerificationAttemptsSummaryList,
)


class Verify(VerifyBase):
    @property
    def forms(self) -> FormList:
        pass

    @property
    def safelist(self) -> SafelistList:
        pass

    @property
    def services(self) -> ServiceList:
        pass

    @property
    def verification_attempts(self) -> VerificationAttemptList:
        pass

    @property
    def verification_attempts_summary(self) -> VerificationAttemptsSummaryList:
        pass

    @property
    def templates(self) -> TemplateList:
        pass
