from warnings import warn

from twilio.rest.messaging.MessagingBase import MessagingBase
from twilio.rest.messaging.v1.brand_registration import BrandRegistrationList
from twilio.rest.messaging.v1.deactivations import DeactivationsList
from twilio.rest.messaging.v1.domain_certs import DomainCertsList
from twilio.rest.messaging.v1.domain_config import DomainConfigList
from twilio.rest.messaging.v1.domain_config_messaging_service import (
    DomainConfigMessagingServiceList,
)
from twilio.rest.messaging.v1.external_campaign import ExternalCampaignList
from twilio.rest.messaging.v1.linkshortening_messaging_service import (
    LinkshorteningMessagingServiceList,
)
from twilio.rest.messaging.v1.service import ServiceList
from twilio.rest.messaging.v1.usecase import UsecaseList


class Messaging(MessagingBase):
    @property
    def brand_registrations(self) -> BrandRegistrationList:
        pass

    @property
    def deactivations(self) -> DeactivationsList:
        pass

    @property
    def domain_certs(self) -> DomainCertsList:
        pass

    @property
    def domain_config(self) -> DomainConfigList:
        pass

    @property
    def domain_config_messaging_service(self) -> DomainConfigMessagingServiceList:
        pass

    @property
    def external_campaign(self) -> ExternalCampaignList:
        pass

    @property
    def linkshortening_messaging_service(self) -> LinkshorteningMessagingServiceList:
        pass

    @property
    def services(self) -> ServiceList:
        pass

    @property
    def usecases(self) -> UsecaseList:
        pass
