from twilio.jwt.access_token import AccessTokenGrant
import warnings
import functools


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    pass


class ChatGrant(AccessTokenGrant):
    """Grant to access Twilio Chat"""

    def __init__(
        self,
        service_sid=None,
        endpoint_id=None,
        deployment_role_sid=None,
        push_credential_sid=None,
    ):
        self.service_sid = service_sid
        self.endpoint_id = endpoint_id
        self.deployment_role_sid = deployment_role_sid
        self.push_credential_sid = push_credential_sid

    @property
    def key(self):
        pass

    def to_payload(self):
        pass


class SyncGrant(AccessTokenGrant):
    """Grant to access Twilio Sync"""

    def __init__(self, service_sid=None, endpoint_id=None):
        self.service_sid = service_sid
        self.endpoint_id = endpoint_id

    @property
    def key(self):
        pass

    def to_payload(self):
        pass


class VoiceGrant(AccessTokenGrant):
    """Grant to access Twilio Programmable Voice"""

    def __init__(
        self,
        incoming_allow=None,
        outgoing_application_sid=None,
        outgoing_application_params=None,
        push_credential_sid=None,
        endpoint_id=None,
    ):
        self.incoming_allow = incoming_allow
        """ :type : bool """
        self.outgoing_application_sid = outgoing_application_sid
        """ :type : str """
        self.outgoing_application_params = outgoing_application_params
        """ :type : dict """
        self.push_credential_sid = push_credential_sid
        """ :type : str """
        self.endpoint_id = endpoint_id
        """ :type : str """

    @property
    def key(self):
        pass

    def to_payload(self):
        pass


class VideoGrant(AccessTokenGrant):
    """Grant to access Twilio Video"""

    def __init__(self, room=None):
        self.room = room

    @property
    def key(self):
        pass

    def to_payload(self):
        pass


class TaskRouterGrant(AccessTokenGrant):
    """Grant to access Twilio TaskRouter"""

    def __init__(self, workspace_sid=None, worker_sid=None, role=None):
        self.workspace_sid = workspace_sid
        self.worker_sid = worker_sid
        self.role = role

    @property
    def key(self):
        pass

    def to_payload(self):
        pass


class PlaybackGrant(AccessTokenGrant):
    """Grant to access Twilio Live stream"""

    def __init__(self, grant=None):
        """Initialize a PlaybackGrant with a grant retrieved from the Twilio API."""
        self.grant = grant

    @property
    def key(self):
        """Return the grant's key."""
        pass

    def to_payload(self):
        """Return the grant."""
        pass
