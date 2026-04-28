import base64
import hmac
from hashlib import sha1, sha256

from urllib.parse import urlparse, parse_qs


def compare(string1, string2):
    """Compare two strings while protecting against timing attacks

    :param str string1: the first string
    :param str string2: the second string

    :returns: True if the strings are equal, False if not
    :rtype: :obj:`bool`
    """
    pass


def remove_port(uri):
    """Remove the port number from a URI

    :param uri: parsed URI that Twilio requested on your server

    :returns: full URI without a port number
    :rtype: str
    """
    pass


def add_port(uri):
    """Add the port number to a URI

    :param uri: parsed URI that Twilio requested on your server

    :returns: full URI with a port number
    :rtype: str
    """
    pass


class RequestValidator(object):
    def __init__(self, token):
        self.token = token.encode("utf-8")

    def compute_signature(self, uri, params):
        """Compute the signature for a given request

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request

        :returns: The computed signature
        """
        pass

    def get_values(self, param_dict, param_name):
        pass

    def compute_hash(self, body):
        pass

    def validate(self, uri, params, signature):
        """Validate a request from Twilio

        :param uri: full URI that Twilio requested on your server
        :param params: dictionary of POST variables or string of POST body for JSON requests
        :param signature: expected signature in HTTP X-Twilio-Signature header

        :returns: True if the request passes validation, False if not
        """
        pass
