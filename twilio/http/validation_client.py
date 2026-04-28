from collections import namedtuple

from requests import Request, Session

from twilio.base.exceptions import TwilioRestException
from urllib.parse import urlparse
from twilio.http import HttpClient
from twilio.http.response import Response
from twilio.jwt.validation import ClientValidationJwt

ValidationPayload = namedtuple(
    "ValidationPayload",
    ["method", "path", "query_string", "all_headers", "signed_headers", "body"],
)


class ValidationClient(HttpClient):
    __SIGNED_HEADERS = ["authorization", "host"]

    def __init__(
        self,
        account_sid,
        api_key_sid,
        credential_sid,
        private_key,
        pool_connections=True,
    ):
        """
        Build a ValidationClient which signs requests with private_key and allows Twilio to
        validate request has not been tampered with.

        :param str account_sid: A Twilio Account Sid starting with 'AC'
        :param str api_key_sid: A Twilio API Key Sid starting with 'SK'
        :param str credential_sid: A Credential Sid starting with 'CR',
                                   corresponds to public key Twilio will use to verify the JWT.
        :param str private_key: The private key used to sign the Client Validation JWT.
        """
        self.account_sid = account_sid
        self.credential_sid = credential_sid
        self.api_key_sid = api_key_sid
        self.private_key = private_key
        self.session = Session() if pool_connections else None

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        """
        Make a signed HTTP Request

        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple auth: Basic Auth arguments
        :param float timeout: Socket/Read timeout for the request
        :param boolean allow_redirects: Whether or not to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An http response
        :rtype: A :class:`Response <twilio.rest.http.response.Response>` object
        """
        pass

    def _build_validation_payload(self, request):
        """
        Extract relevant information from request to build a ClientValidationJWT
        :param PreparedRequest request: request we will extract information from.
        :return: ValidationPayload
        """
        pass

    def _get_host(self, request):
        """Pull the Host out of the request"""
        pass

    def validate_ssl_certificate(self, client):
        """
        Validate that a request to the new SSL certificate is successful
        :return: null on success, raise TwilioRestException if the request fails
        """
        pass
