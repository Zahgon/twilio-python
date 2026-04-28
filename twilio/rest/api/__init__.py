from warnings import warn

from twilio.rest.api.ApiBase import ApiBase
from twilio.rest.api.v2010.account import AccountContext, AccountList
from twilio.rest.api.v2010.account.address import AddressList
from twilio.rest.api.v2010.account.application import ApplicationList
from twilio.rest.api.v2010.account.authorized_connect_app import (
    AuthorizedConnectAppList,
)
from twilio.rest.api.v2010.account.available_phone_number_country import (
    AvailablePhoneNumberCountryList,
)
from twilio.rest.api.v2010.account.balance import BalanceList
from twilio.rest.api.v2010.account.call import CallList
from twilio.rest.api.v2010.account.conference import ConferenceList
from twilio.rest.api.v2010.account.connect_app import ConnectAppList
from twilio.rest.api.v2010.account.incoming_phone_number import IncomingPhoneNumberList
from twilio.rest.api.v2010.account.key import KeyList
from twilio.rest.api.v2010.account.message import MessageList
from twilio.rest.api.v2010.account.new_key import NewKeyList
from twilio.rest.api.v2010.account.new_signing_key import NewSigningKeyList
from twilio.rest.api.v2010.account.notification import NotificationList
from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
from twilio.rest.api.v2010.account.queue import QueueList
from twilio.rest.api.v2010.account.recording import RecordingList
from twilio.rest.api.v2010.account.short_code import ShortCodeList
from twilio.rest.api.v2010.account.signing_key import SigningKeyList
from twilio.rest.api.v2010.account.sip import SipList
from twilio.rest.api.v2010.account.token import TokenList
from twilio.rest.api.v2010.account.transcription import TranscriptionList
from twilio.rest.api.v2010.account.usage import UsageList
from twilio.rest.api.v2010.account.validation_request import ValidationRequestList


class Api(ApiBase):
    @property
    def account(self) -> AccountContext:
        pass

    @property
    def accounts(self) -> AccountList:
        pass

    @property
    def addresses(self) -> AddressList:
        pass

    @property
    def applications(self) -> ApplicationList:
        pass

    @property
    def authorized_connect_apps(self) -> AuthorizedConnectAppList:
        pass

    @property
    def available_phone_numbers(self) -> AvailablePhoneNumberCountryList:
        pass

    @property
    def balance(self) -> BalanceList:
        pass

    @property
    def calls(self) -> CallList:
        pass

    @property
    def conferences(self) -> ConferenceList:
        pass

    @property
    def connect_apps(self) -> ConnectAppList:
        pass

    @property
    def incoming_phone_numbers(self) -> IncomingPhoneNumberList:
        pass

    @property
    def keys(self) -> KeyList:
        pass

    @property
    def messages(self) -> MessageList:
        pass

    @property
    def new_keys(self) -> NewKeyList:
        pass

    @property
    def new_signing_keys(self) -> NewSigningKeyList:
        pass

    @property
    def notifications(self) -> NotificationList:
        pass

    @property
    def outgoing_caller_ids(self) -> OutgoingCallerIdList:
        pass

    @property
    def queues(self) -> QueueList:
        pass

    @property
    def recordings(self) -> RecordingList:
        pass

    @property
    def signing_keys(self) -> SigningKeyList:
        pass

    @property
    def sip(self) -> SipList:
        pass

    @property
    def short_codes(self) -> ShortCodeList:
        pass

    @property
    def tokens(self) -> TokenList:
        pass

    @property
    def transcriptions(self) -> TranscriptionList:
        pass

    @property
    def usage(self) -> UsageList:
        pass

    @property
    def validation_requests(self) -> ValidationRequestList:
        pass
