from warnings import warn

from twilio.rest.chat.ChatBase import ChatBase
from twilio.rest.chat.v2.credential import CredentialList
from twilio.rest.chat.v2.service import ServiceList
from twilio.rest.chat.v3.channel import ChannelList


class Chat(ChatBase):
    @property
    def credentials(self) -> CredentialList:
        pass

    @property
    def services(self) -> ServiceList:
        pass

    @property
    def channels(self) -> ChannelList:
        pass
