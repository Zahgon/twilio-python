from warnings import warn

from twilio.rest.voice.VoiceBase import VoiceBase
from twilio.rest.voice.v1.archived_call import ArchivedCallList
from twilio.rest.voice.v1.byoc_trunk import ByocTrunkList
from twilio.rest.voice.v1.connection_policy import ConnectionPolicyList
from twilio.rest.voice.v1.dialing_permissions import DialingPermissionsList
from twilio.rest.voice.v1.ip_record import IpRecordList
from twilio.rest.voice.v1.source_ip_mapping import SourceIpMappingList


class Voice(VoiceBase):
    @property
    def archived_calls(self) -> ArchivedCallList:
        pass

    @property
    def byoc_trunks(self) -> ByocTrunkList:
        pass

    @property
    def connection_policies(self) -> ConnectionPolicyList:
        pass

    @property
    def dialing_permissions(self) -> DialingPermissionsList:
        pass

    @property
    def ip_records(self) -> IpRecordList:
        pass

    @property
    def source_ip_mappings(self) -> SourceIpMappingList:
        pass
