from warnings import warn

from twilio.rest.trusthub.TrusthubBase import TrusthubBase
from twilio.rest.trusthub.v1.customer_profiles import CustomerProfilesList
from twilio.rest.trusthub.v1.end_user import EndUserList
from twilio.rest.trusthub.v1.end_user_type import EndUserTypeList
from twilio.rest.trusthub.v1.policies import PoliciesList
from twilio.rest.trusthub.v1.supporting_document import SupportingDocumentList
from twilio.rest.trusthub.v1.supporting_document_type import SupportingDocumentTypeList
from twilio.rest.trusthub.v1.trust_products import TrustProductsList


class Trusthub(TrusthubBase):
    @property
    def customer_profiles(self) -> CustomerProfilesList:
        pass

    @property
    def end_users(self) -> EndUserList:
        pass

    @property
    def end_user_types(self) -> EndUserTypeList:
        pass

    @property
    def policies(self) -> PoliciesList:
        pass

    @property
    def supporting_documents(self) -> SupportingDocumentList:
        pass

    @property
    def supporting_document_types(self) -> SupportingDocumentTypeList:
        pass

    @property
    def trust_products(self) -> TrustProductsList:
        pass
