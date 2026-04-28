import json
from typing import Any, Dict, Optional

from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class Page(object):
    """
    Represents a page of records in a collection.

    A `Page` lets you iterate over its records and fetch the next and previous
    pages in the collection.
    """

    META_KEYS = {
        "end",
        "first_page_uri",
        "next_page_uri",
        "last_page_uri",
        "page",
        "page_size",
        "previous_page_uri",
        "total",
        "num_pages",
        "start",
        "uri",
    }

    def __init__(self, version, response: Response, solution={}):
        payload = self.process_response(response)

        self._version = version
        self._payload = payload
        self._solution = solution
        self._records = iter(self.load_page(payload))

    def __iter__(self):
        """
        A `Page` is a valid iterator.
        """
        return self

    def __next__(self):
        return self.next()

    def next(self):
        """
        Returns the next record in the `Page`.
        """
        pass

    @classmethod
    def process_response(cls, response: Response) -> Any:
        """
        Load a JSON response.

        :param response: The HTTP response.
        :return The JSON-loaded content.
        """
        pass

    def load_page(self, payload: Dict[str, Any]):
        """
        Parses the collection of records out of a list payload.

        :param payload: The JSON-loaded content.
        :return list: The list of records.
        """
        pass

    @property
    def previous_page_url(self) -> Optional[str]:
        """
        :return str: Returns a link to the previous_page_url or None if doesn't exist.
        """
        pass

    @property
    def next_page_url(self) -> Optional[str]:
        """
        :return str: Returns a link to the next_page_url or None if doesn't exist.
        """
        pass

    def get_instance(self, payload: Dict[str, Any]) -> Any:
        """
        :param dict payload: A JSON-loaded representation of an instance record.
        :return: A rich, resource-dependent object.
        """
        raise TwilioException(
            "Page.get_instance() must be implemented in the derived class"
        )

    def next_page(self) -> Optional["Page"]:
        """
        Return the `Page` after this one.
        :return The next page.
        """
        pass

    async def next_page_async(self) -> Optional["Page"]:
        """
        Asynchronously return the `Page` after this one.
        :return The next page.
        """
        pass

    def previous_page(self) -> Optional["Page"]:
        """
        Return the `Page` before this one.
        :return The previous page.
        """
        pass

    async def previous_page_async(self) -> Optional["Page"]:
        """
        Asynchronously return the `Page` before this one.
        :return The previous page.
        """
        pass

    def __repr__(self) -> str:
        return "<Page>"
