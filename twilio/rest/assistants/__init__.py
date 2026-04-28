from warnings import warn

from twilio.rest.assistants.AssistantsBase import AssistantsBase
from twilio.rest.assistants.v1.assistant import AssistantList
from twilio.rest.assistants.v1.knowledge import KnowledgeList
from twilio.rest.assistants.v1.policy import PolicyList
from twilio.rest.assistants.v1.session import SessionList
from twilio.rest.assistants.v1.tool import ToolList


class Assistants(AssistantsBase):

    @property
    def assistants(self) -> AssistantList:
        pass

    @property
    def knowledge(self) -> KnowledgeList:
        pass

    @property
    def policies(self) -> PolicyList:
        pass

    @property
    def sessions(self) -> SessionList:
        pass

    @property
    def tools(self) -> ToolList:
        pass
