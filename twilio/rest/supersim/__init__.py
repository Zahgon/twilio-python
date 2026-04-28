from warnings import warn

from twilio.rest.supersim.SupersimBase import SupersimBase
from twilio.rest.supersim.v1.esim_profile import EsimProfileList
from twilio.rest.supersim.v1.fleet import FleetList
from twilio.rest.supersim.v1.ip_command import IpCommandList
from twilio.rest.supersim.v1.network import NetworkList
from twilio.rest.supersim.v1.network_access_profile import NetworkAccessProfileList
from twilio.rest.supersim.v1.settings_update import SettingsUpdateList
from twilio.rest.supersim.v1.sim import SimList
from twilio.rest.supersim.v1.sms_command import SmsCommandList
from twilio.rest.supersim.v1.usage_record import UsageRecordList


class Supersim(SupersimBase):
    @property
    def esim_profiles(self) -> EsimProfileList:
        pass

    @property
    def fleets(self) -> FleetList:
        pass

    @property
    def ip_commands(self) -> IpCommandList:
        pass

    @property
    def networks(self) -> NetworkList:
        pass

    @property
    def network_access_profiles(self) -> NetworkAccessProfileList:
        pass

    @property
    def settings_updates(self) -> SettingsUpdateList:
        pass

    @property
    def sims(self) -> SimList:
        pass

    @property
    def sms_commands(self) -> SmsCommandList:
        pass

    @property
    def usage_records(self) -> UsageRecordList:
        pass
