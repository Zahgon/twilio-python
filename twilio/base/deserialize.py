import datetime
from decimal import BasicContext, Decimal
from email.utils import parsedate
from typing import Optional, Union

ISO8601_DATE_FORMAT = "%Y-%m-%d"
ISO8601_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def iso8601_date(s: str) -> Union[datetime.date, str]:
    """
    Parses an ISO 8601 date string and returns a UTC date object or the string
    if the parsing failed.
    :param s: ISO 8601-formatted date string (2015-01-25)
    :return:
    """
    pass


def iso8601_datetime(
    s: str,
) -> Union[datetime.datetime, str]:
    """
    Parses an ISO 8601 datetime string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: ISO 8601-formatted datetime string (2015-01-25T12:34:56Z)
    """
    pass


def rfc2822_datetime(s: str) -> Optional[datetime.datetime]:
    """
    Parses an RFC 2822 date string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: RFC 2822-formatted string date
    :return: datetime or str
    """
    pass


def decimal(d: Optional[str]) -> Union[Decimal, str]:
    """
    Parses a decimal string into a Decimal
    :param d: decimal string
    """
    pass


def integer(i: str) -> Union[int, str]:
    """
    Parses an integer string into an int
    :param i: integer string
    :return: int
    """
    pass
