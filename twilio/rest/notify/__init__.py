from warnings import warn

from twilio.rest.notify.NotifyBase import NotifyBase
from twilio.rest.notify.v1.credential import CredentialList
from twilio.rest.notify.v1.service import ServiceList


class Notify(NotifyBase):
    @property
    def credentials(self) -> CredentialList:
        pass

    @property
    def services(self) -> ServiceList:
        pass
