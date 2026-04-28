from warnings import warn

from twilio.rest.preview.PreviewBase import PreviewBase
from twilio.rest.preview.hosted_numbers.authorization_document import (
    AuthorizationDocumentList,
)
from twilio.rest.preview.hosted_numbers.hosted_number_order import HostedNumberOrderList
from twilio.rest.preview.marketplace.available_add_on import AvailableAddOnList
from twilio.rest.preview.marketplace.installed_add_on import InstalledAddOnList
from twilio.rest.preview.wireless.command import CommandList
from twilio.rest.preview.wireless.rate_plan import RatePlanList
from twilio.rest.preview.wireless.sim import SimList


class Preview(PreviewBase):

    @property
    def authorization_documents(self) -> AuthorizationDocumentList:
        pass

    @property
    def hosted_number_orders(self) -> HostedNumberOrderList:
        pass

    @property
    def available_add_ons(self) -> AvailableAddOnList:
        pass

    @property
    def installed_add_ons(self) -> InstalledAddOnList:
        pass

    @property
    def commands(self) -> CommandList:
        pass

    @property
    def rate_plans(self) -> RatePlanList:
        pass

    @property
    def sims(self) -> SimList:
        pass
