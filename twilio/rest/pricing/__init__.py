from warnings import warn

from twilio.rest.pricing.PricingBase import PricingBase
from twilio.rest.pricing.v1.messaging import MessagingList
from twilio.rest.pricing.v1.phone_number import PhoneNumberList
from twilio.rest.pricing.v2.country import CountryList
from twilio.rest.pricing.v2.number import NumberList
from twilio.rest.pricing.v2.voice import VoiceList


class Pricing(PricingBase):
    @property
    def messaging(self) -> MessagingList:
        pass

    @property
    def phone_numbers(self) -> PhoneNumberList:
        pass

    @property
    def voice(self) -> VoiceList:
        pass

    @property
    def countries(self) -> CountryList:
        pass

    @property
    def numbers(self) -> NumberList:
        pass
