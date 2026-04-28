from warnings import warn

from twilio.rest.numbers.NumbersBase import NumbersBase
from twilio.rest.numbers.v2.regulatory_compliance import RegulatoryComplianceList


class Numbers(NumbersBase):
    @property
    def regulatory_compliance(self) -> RegulatoryComplianceList:
        pass
