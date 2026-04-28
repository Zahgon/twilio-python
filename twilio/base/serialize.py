import datetime
import json

from twilio.base import values


def iso8601_date(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    pass


def iso8601_datetime(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    pass


def prefixed_collapsible_map(m, prefix):
    """
    Return a dict of params corresponding to those in m with the added prefix
    """
    pass


def boolean_to_string(bool_or_str):
    pass


def object(obj):
    """
    Return a jsonified string represenation of obj if obj is jsonifiable else
    return obj untouched
    """
    pass


def map(lst, serialize_func):
    """
    Applies serialize_func to every element in lst
    """
    pass
