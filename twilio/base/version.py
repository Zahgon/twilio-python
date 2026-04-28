import json
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Tuple, Union

from twilio.base import values
from twilio.base.domain import Domain
from twilio.base.exceptions import TwilioRestException, TwilioServiceException
from twilio.base.page import Page
from twilio.http.response import Response


class Version(object):
    """
    Represents an API version.
    """

    def __init__(self, domain: Domain, version: str):
        self.domain = domain
        self.version = version

    def absolute_url(self, uri: str) -> str:
        """
        Turns a relative uri into an absolute url.
        """
        pass

    def relative_uri(self, uri: str) -> str:
        """
        Turns a relative uri into a versioned relative uri.
        """
        pass

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
        Make an HTTP request.
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
        Make an asynchronous HTTP request
        """
        pass

    @classmethod
    def exception(
        cls, method: str, uri: str, response: Response, message: str
    ) -> Union[TwilioRestException, TwilioServiceException]:
        """
        Wraps an exceptional response in a `TwilioRestException` or `TwilioServiceException`.

        If the response is RFC-9457 compliant (contains 'type', 'title', 'status', and 'code' fields),
        returns a TwilioServiceException. Otherwise, returns a TwilioRestException for backward compatibility.
        """
        pass

    def _parse_fetch(self, method: str, uri: str, response: Response) -> Any:
        """
        Parses fetch response JSON
        """
        pass

    def fetch(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Fetch a resource instance.
        """
        pass

    async def fetch_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Asynchronously fetch a resource instance.
        """
        pass

    def fetch_with_response_info(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Fetch a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (typically 200)
                - headers_dict: Response headers as a dictionary
        """
        pass

    async def fetch_with_response_info_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Asynchronously fetch a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (typically 200)
                - headers_dict: Response headers as a dictionary
        """
        pass

    def _parse_update(self, method: str, uri: str, response: Response) -> Any:
        """
        Parses update response JSON
        """
        pass

    def update(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Update a resource instance.
        """
        pass

    async def update_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Asynchronously update a resource instance.
        """
        pass

    def update_with_response_info(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Update a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (typically 200)
                - headers_dict: Response headers as a dictionary
        """
        pass

    async def update_with_response_info_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Asynchronously update a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (typically 200)
                - headers_dict: Response headers as a dictionary
        """
        pass

    def _parse_delete(self, method: str, uri: str, response: Response) -> bool:
        """
        Parses delete response JSON
        """
        pass

    def delete(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> bool:
        """
        Delete a resource.
        """
        pass

    async def delete_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> bool:
        """
        Asynchronously delete a resource.
        """
        pass

    def delete_with_response_info(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[bool, int, Dict[str, str]]:
        """
        Delete a resource and return response metadata

        Returns:
            tuple: (success_boolean, status_code, headers_dict)
                - success_boolean: True if deletion was successful (2XX response)
                - status_code: HTTP status code (typically 204 for successful delete)
                - headers_dict: Response headers as a dictionary
        """
        pass

    async def delete_with_response_info_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[bool, int, Dict[str, str]]:
        """
        Asynchronously delete a resource and return response metadata

        Returns:
            tuple: (success_boolean, status_code, headers_dict)
                - success_boolean: True if deletion was successful (2XX response)
                - status_code: HTTP status code (typically 204 for successful delete)
                - headers_dict: Response headers as a dictionary
        """
        pass

    def read_limits(
        self, limit: Optional[int] = None, page_size: Optional[int] = None
    ) -> Dict[str, object]:
        """
        Takes a limit on the max number of records to read and a max page_size
        and calculates the max number of pages to read.

        :param limit: Max number of records to read.
        :param page_size: Max page size.
        :return A dictionary of paging limits.
        """
        pass

    def page(
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
        Makes an HTTP request.
        """
        pass

    async def page_async(
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
        Makes an asynchronous HTTP request.
        """
        pass

    def page_with_response_info(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Response, int, Dict[str, str]]:
        """
        Fetch a page and return response metadata

        Returns:
            tuple: (response_object, status_code, headers_dict)
                - response_object: The Response object (not parsed JSON)
                - status_code: HTTP status code
                - headers_dict: Response headers as a dictionary
        """
        pass

    async def page_with_response_info_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Response, int, Dict[str, str]]:
        """
        Asynchronously fetch a page and return response metadata

        Returns:
            tuple: (response_object, status_code, headers_dict)
                - response_object: The Response object (not parsed JSON)
                - status_code: HTTP status code
                - headers_dict: Response headers as a dictionary
        """
        pass

    def stream(
        self,
        page: Optional[Page],
        limit: Optional[int] = None,
        page_limit: Optional[int] = None,
    ) -> Iterator[Any]:
        """
        Generates records one a time from a page, stopping at prescribed limits.

        :param page: The page to stream.
        :param limit: The max number of records to read.
        :param page_limit: The max number of pages to read.
        """
        pass

    async def stream_async(
        self,
        page: Optional[Page],
        limit: Optional[int] = None,
        page_limit: Optional[int] = None,
    ) -> AsyncIterator[Any]:
        """
        Generates records one a time from a page, stopping at prescribed limits.

        :param page: The page to stream.
        :param limit: The max number of records to read.
        :param page_limit: The max number of pages to read.
        """
        pass

    def _parse_create(self, method: str, uri: str, response: Response) -> Any:
        """
        Parse create response JSON
        """
        pass

    def create(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Create a resource instance.
        """
        pass

    async def create_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Any:
        """
        Asynchronously create a resource instance.
        """
        pass

    def create_with_response_info(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Create a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (e.g., 201)
                - headers_dict: Response headers as a dictionary
        """
        pass

    async def create_with_response_info_async(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Tuple[Any, int, Dict[str, str]]:
        """
        Asynchronously create a resource and return response metadata

        Returns:
            tuple: (payload_dict, status_code, headers_dict)
                - payload_dict: The JSON response body as a dictionary
                - status_code: HTTP status code (e.g., 201)
                - headers_dict: Response headers as a dictionary
        """
        pass
