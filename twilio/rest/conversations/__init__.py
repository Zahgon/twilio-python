from warnings import warn

from twilio.rest.conversations.ConversationsBase import ConversationsBase
from twilio.rest.conversations.v1.address_configuration import AddressConfigurationList
from twilio.rest.conversations.v1.configuration import ConfigurationList
from twilio.rest.conversations.v1.conversation import ConversationList
from twilio.rest.conversations.v1.credential import CredentialList
from twilio.rest.conversations.v1.participant_conversation import (
    ParticipantConversationList,
)
from twilio.rest.conversations.v1.role import RoleList
from twilio.rest.conversations.v1.service import ServiceList
from twilio.rest.conversations.v1.user import UserList


class Conversations(ConversationsBase):
    @property
    def configuration(self) -> ConfigurationList:
        pass

    @property
    def address_configurations(self) -> AddressConfigurationList:
        pass

    @property
    def conversations(self) -> ConversationList:
        pass

    @property
    def credentials(self) -> CredentialList:
        pass

    @property
    def participant_conversations(self) -> ParticipantConversationList:
        pass

    @property
    def roles(self) -> RoleList:
        pass

    @property
    def services(self) -> ServiceList:
        pass

    @property
    def users(self) -> UserList:
        pass
