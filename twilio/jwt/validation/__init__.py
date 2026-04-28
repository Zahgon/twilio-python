from hashlib import sha256

from twilio.jwt import Jwt


class ClientValidationJwt(Jwt):
    """A JWT included on requests so that Twilio can verify request authenticity"""

    __CTY = "twilio-pkrv;v=1"
    ALGORITHM = "RS256"

    def __init__(
        self, account_sid, api_key_sid, credential_sid, private_key, validation_payload
    ):
        """
        Create a new ClientValidationJwt
        :param str account_sid: A Twilio Account Sid starting with 'AC'
        :param str api_key_sid: A Twilio API Key Sid starting with 'SK'
        :param str credential_sid: A Credential Sid starting with 'CR',
                                   public key Twilio will use to verify the JWT.
        :param str private_key: The private key used to sign the JWT.
        :param ValidationPayload validation_payload: information from the request to sign
        """
        super(ClientValidationJwt, self).__init__(
            secret_key=private_key,
            issuer=api_key_sid,
            subject=account_sid,
            algorithm=self.ALGORITHM,
            ttl=300,  # 5 minute ttl
        )
        self.credential_sid = credential_sid
        self.validation_payload = validation_payload

    def _generate_headers(self):
        pass

    def _generate_payload(self):
        # Lowercase header keys, combine and sort headers with list values
        pass

    @classmethod
    def _sort_and_join(cls, values, joiner):
        pass

    @classmethod
    def _hash(cls, input_str):
        pass
