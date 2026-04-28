import warnings
import functools


class ObsoleteException(Exception):
    """Base class for warnings about obsolete features."""


def obsolete_client(func):
    """This is a decorator which can be used to mark Client classes as
    obsolete. It will result in an error being emitted when the class is
    instantiated."""
    pass


def deprecated_method(new_func=None):
    """
    This is a decorator which can be used to mark deprecated methods.
    It will report in a DeprecationWarning being emitted to stderr when the deprecated method is used.
    """
    pass
