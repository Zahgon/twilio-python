from warnings import warn

from twilio.rest.video.VideoBase import VideoBase
from twilio.rest.video.v1.composition import CompositionList
from twilio.rest.video.v1.composition_hook import CompositionHookList
from twilio.rest.video.v1.composition_settings import CompositionSettingsList
from twilio.rest.video.v1.recording import RecordingList
from twilio.rest.video.v1.recording_settings import RecordingSettingsList
from twilio.rest.video.v1.room import RoomList


class Video(VideoBase):
    @property
    def compositions(self) -> CompositionList:
        pass

    @property
    def composition_hooks(self) -> CompositionHookList:
        pass

    @property
    def composition_settings(self) -> CompositionSettingsList:
        pass

    @property
    def recordings(self) -> RecordingList:
        pass

    @property
    def recording_settings(self) -> RecordingSettingsList:
        pass

    @property
    def rooms(self) -> RoomList:
        pass
