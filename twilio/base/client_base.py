import os
import platform
from typing import Dict, List, MutableMapping, Optional, Tuple
from urllib.parse import urlparse, urlunparse

from twilio import __version__
from twilio.http import HttpClient
from twilio.http.http_client import TwilioHttpClient
from twilio.http.response import Response
from twilio.credential.credential_provider import CredentialProvider


class ClientBase(object):
    """A client for accessing the Twilio API."""

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        account_sid: Optional[str] = None,
        region: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
        environment: Optional[MutableMapping[str, str]] = None,
        edge: Optional[str] = None,
        user_agent_extensions: Optional[List[str]] = None,
        credential_provider: Optional[CredentialProvider] = None,
    ):
        """
        Initializes the Twilio Client

        :param username: Username to authenticate with
        :param password: Password to authenticate with
        :param account_sid: Account SID, defaults to Username
        :param region: Twilio Region to make requests to, defaults to 'us1' if an edge is provided
        :param http_client: HttpClient, defaults to TwilioHttpClient
        :param environment: Environment to look for auth details, defaults to os.environ
        :param edge: Twilio Edge to make requests to, defaults to None.
        :param user_agent_extensions: Additions to the user agent string
        :param credential_provider: credential provider for authentication method that needs to be used
        """

        environment = environment or os.environ

        self.username = username or environment.get("TWILIO_ACCOUNT_SID")
        """ :type : str """
        self.password = password or environment.get("TWILIO_AUTH_TOKEN")
        """ :type : str """
        self.edge = edge or environment.get("TWILIO_EDGE")
        """ :type : str """
        self.region = region or environment.get("TWILIO_REGION")
        """ :type : str """
        self.user_agent_extensions = user_agent_extensions or []
        """ :type : list[str] """
        self.credential_provider = credential_provider or None
        """ :type : CredentialProvider """

        self.account_sid = account_sid or self.username
        """ :type : str """
        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client: HttpClient = http_client or TwilioHttpClient()
        """ :type : HttpClient """

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided

        :param method: HTTP Method
        :param uri: Fully qualified url
        :param params: Query string parameters
        :param data: POST body data
        :param headers: HTTP Headers
        :param auth: Authentication
        :param timeout: Timeout in seconds
        :param allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        """
        pass

    async def request_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Asynchronously makes a request to the Twilio API  using the configured http client
        The configured http client must be an asynchronous http client
        Authentication information is automatically added if none is provided

        :param method: HTTP Method
        :param uri: Fully qualified url
        :param params: Query string parameters
        :param data: POST body data
        :param headers: HTTP Headers
        :param auth: Authentication
        :param timeout: Timeout in seconds
        :param allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        """
        pass

    def copy_non_none_values(self, data):
        pass

    def get_auth(self, auth: Optional[Tuple[str, str]]) -> Tuple[str, str]:
        """
        Get the request authentication object
        :param auth: Authentication (username, password)
        :returns: The authentication object
        """
        pass

    def get_headers(
        self, method: str, headers: Optional[Dict[str, str]]
    ) -> Dict[str, str]:
        """
        Get the request headers including user-agent, extensions, encoding, content-type, MIME type
        :param method: HTTP method
        :param headers: HTTP headers
        :returns: HTTP headers
        """
        pass

    def get_hostname(self, uri: str) -> str:
        """
        Determines the proper hostname given edge and region preferences
        via client configuration or uri.

        :param uri: Fully qualified url

        :returns: The final uri used to make the request
        """
        pass

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio {}>".format(self.account_sid)
