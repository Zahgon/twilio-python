from warnings import warn

from twilio.rest.flex_api.FlexApiBase import FlexApiBase
from twilio.rest.flex_api.v1.assessments import AssessmentsList
from twilio.rest.flex_api.v1.channel import ChannelList
from twilio.rest.flex_api.v1.configuration import ConfigurationList
from twilio.rest.flex_api.v1.flex_flow import FlexFlowList
from twilio.rest.flex_api.v1.insights_assessments_comment import (
    InsightsAssessmentsCommentList,
)
from twilio.rest.flex_api.v1.insights_conversations import InsightsConversationsList
from twilio.rest.flex_api.v1.insights_questionnaires import InsightsQuestionnairesList
from twilio.rest.flex_api.v1.insights_questionnaires_category import (
    InsightsQuestionnairesCategoryList,
)
from twilio.rest.flex_api.v1.insights_questionnaires_question import (
    InsightsQuestionnairesQuestionList,
)
from twilio.rest.flex_api.v1.insights_segments import InsightsSegmentsList
from twilio.rest.flex_api.v1.insights_session import InsightsSessionList
from twilio.rest.flex_api.v1.insights_settings_answer_sets import (
    InsightsSettingsAnswerSetsList,
)
from twilio.rest.flex_api.v1.insights_settings_comment import (
    InsightsSettingsCommentList,
)
from twilio.rest.flex_api.v1.insights_user_roles import InsightsUserRolesList
from twilio.rest.flex_api.v1.interaction import InteractionList
from twilio.rest.flex_api.v1.web_channel import WebChannelList
from twilio.rest.flex_api.v2.web_channels import WebChannelsList


class FlexApi(FlexApiBase):
    @property
    def assessments(self) -> AssessmentsList:
        pass

    @property
    def channel(self) -> ChannelList:
        pass

    @property
    def configuration(self) -> ConfigurationList:
        pass

    @property
    def flex_flow(self) -> FlexFlowList:
        pass

    @property
    def insights_assessments_comment(self) -> InsightsAssessmentsCommentList:
        pass

    @property
    def insights_conversations(self) -> InsightsConversationsList:
        pass

    @property
    def insights_questionnaires(self) -> InsightsQuestionnairesList:
        pass

    @property
    def insights_questionnaires_category(self) -> InsightsQuestionnairesCategoryList:
        pass

    @property
    def insights_questionnaires_question(self) -> InsightsQuestionnairesQuestionList:
        pass

    @property
    def insights_segments(self) -> InsightsSegmentsList:
        pass

    @property
    def insights_session(self) -> InsightsSessionList:
        pass

    @property
    def insights_settings_answer_sets(self) -> InsightsSettingsAnswerSetsList:
        pass

    @property
    def insights_settings_comment(self) -> InsightsSettingsCommentList:
        pass

    @property
    def insights_user_roles(self) -> InsightsUserRolesList:
        pass

    @property
    def interaction(self) -> InteractionList:
        pass

    @property
    def web_channel(self) -> WebChannelList:
        pass

    @property
    def web_channels(self) -> WebChannelsList:
        pass
