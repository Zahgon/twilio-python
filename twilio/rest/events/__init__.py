from warnings import warn

from twilio.rest.events.EventsBase import EventsBase
from twilio.rest.events.v1.event_type import EventTypeList
from twilio.rest.events.v1.schema import SchemaList
from twilio.rest.events.v1.sink import SinkList
from twilio.rest.events.v1.subscription import SubscriptionList


class Events(EventsBase):
    @property
    def event_types(self) -> EventTypeList:
        pass

    @property
    def schemas(self) -> SchemaList:
        pass

    @property
    def sinks(self) -> SinkList:
        pass

    @property
    def subscriptions(self) -> SubscriptionList:
        pass
