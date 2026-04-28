from warnings import warn

from twilio.rest.studio.StudioBase import StudioBase
from twilio.rest.studio.v2.flow import FlowList
from twilio.rest.studio.v2.flow_validate import FlowValidateList


class Studio(StudioBase):
    @property
    def flows(self) -> FlowList:
        pass

    @property
    def flow_validate(self) -> FlowValidateList:
        pass
