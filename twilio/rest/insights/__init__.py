from warnings import warn

from twilio.rest.insights.InsightsBase import InsightsBase
from twilio.rest.insights.v1.call import CallList
from twilio.rest.insights.v1.call_summaries import CallSummariesList
from twilio.rest.insights.v1.conference import ConferenceList
from twilio.rest.insights.v1.room import RoomList
from twilio.rest.insights.v1.setting import SettingList


class Insights(InsightsBase):
    @property
    def settings(self) -> SettingList:
        pass

    @property
    def calls(self) -> CallList:
        pass

    @property
    def call_summaries(self) -> CallSummariesList:
        pass

    @property
    def conferences(self) -> ConferenceList:
        pass

    @property
    def rooms(self) -> RoomList:
        pass
