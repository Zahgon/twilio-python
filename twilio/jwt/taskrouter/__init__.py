from twilio.jwt import Jwt


class TaskRouterCapabilityToken(Jwt):
    VERSION = "v1"
    DOMAIN = "https://taskrouter.twilio.com"
    EVENTS_BASE_URL = "https://event-bridge.twilio.com/v1/wschannels"
    ALGORITHM = "HS256"

    def __init__(self, account_sid, auth_token, workspace_sid, channel_id, **kwargs):
        """
        :param str account_sid: Twilio account sid
        :param str auth_token: Twilio auth token used to sign the JWT
        :param str workspace_sid: TaskRouter workspace sid
        :param str channel_id: TaskRouter channel sid
        :param kwargs:
            :param bool allow_web_sockets: shortcut to calling allow_web_sockets, defaults to True
            :param bool allow_fetch_self: shortcut to calling allow_fetch_self, defaults to True
            :param bool allow_update_self: shortcut to calling allow_update_self, defaults to False
            :param bool allow_delete_self: shortcut to calling allow_delete_self, defaults to False
            :param bool allow_fetch_subresources: shortcut to calling allow_fetch_subresources,
                                                  defaults to False
            :param bool allow_update_subresources: shortcut to calling allow_update_subresources,
                                                   defaults to False
            :param bool allow_delete_subresources: shortcut to calling allow_delete_subresources,
                                                   defaults to False
        :returns a new TaskRouterCapabilityToken with capabilities set depending on kwargs.
        """
        super(TaskRouterCapabilityToken, self).__init__(
            secret_key=auth_token,
            issuer=account_sid,
            algorithm=self.ALGORITHM,
            nbf=kwargs.get("nbf", Jwt.GENERATE),
            ttl=kwargs.get("ttl", 3600),
            valid_until=kwargs.get("valid_until", None),
        )

        self._validate_inputs(account_sid, workspace_sid, channel_id)

        self.account_sid = account_sid
        self.auth_token = auth_token
        self.workspace_sid = workspace_sid
        self.channel_id = channel_id
        self.policies = []

        if kwargs.get("allow_web_sockets", True):
            self.allow_web_sockets()
        if kwargs.get("allow_fetch_self", True):
            self.allow_fetch_self()
        if kwargs.get("allow_update_self", False):
            self.allow_update_self()
        if kwargs.get("allow_delete_self", False):
            self.allow_delete_self()
        if kwargs.get("allow_fetch_subresources", False):
            self.allow_fetch_subresources()
        if kwargs.get("allow_delete_subresources", False):
            self.allow_delete_subresources()
        if kwargs.get("allow_update_subresources", False):
            self.allow_update_subresources()

    @property
    def workspace_url(self):
        pass

    @property
    def resource_url(self):
        raise NotImplementedError("Subclass must set its specific resource_url.")

    @property
    def channel_prefix(self):
        raise NotImplementedError(
            "Subclass must set its specific channel_id sid prefix."
        )

    def allow_fetch_self(self):
        pass

    def allow_update_self(self):
        pass

    def allow_delete_self(self):
        pass

    def allow_fetch_subresources(self):
        pass

    def allow_update_subresources(self):
        pass

    def allow_delete_subresources(self):
        pass

    def allow_web_sockets(self, channel_id=None):
        pass

    def _generate_payload(self):
        pass

    def _make_policy(self, url, method, allowed, query_filter=None, post_filter=None):
        pass

    def _validate_inputs(self, account_sid, workspace_sid, channel_id):
        pass

    def __str__(self):
        return "<TaskRouterCapabilityToken {}>".format(self.to_jwt())
