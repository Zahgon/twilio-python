import json
import re
import xml.etree.ElementTree as ET


def lower_camel(string):
    pass


def format_language(language):
    """
    Attempt to format language parameter as 'ww-WW'.

    :param string language: language parameter
    """
    pass


class TwiMLException(Exception):
    pass


class TwiML(object):
    MAP = {
        "from_": "from",
        "xml_lang": "xml:lang",
        "interpret_as": "interpret-as",
        "for_": "for",
        "break_": "break",
    }

    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.value = None
        self.verbs = []
        self.attrs = {}

        for k, v in kwargs.items():
            if v is not None:
                self.attrs[lower_camel(self.MAP.get(k, k))] = v

    def __str__(self):
        return self.to_xml()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def to_xml(self, xml_declaration=True):
        """
        Return the contents of this verb as an XML string

        :param bool xml_declaration: Include the XML declaration. Defaults to True
        """
        pass

    def append(self, verb):
        """
        Add a TwiML doc

        :param verb: TwiML Document

        :returns: self
        """
        pass

    def nest(self, verb):
        """
        Add a TwiML doc. Unlike `append()`, this returns the created verb.

        :param verb: TwiML Document

        :returns: the TwiML verb
        """
        pass

    def xml(self):
        pass

    def add_child(self, name, value=None, **kwargs):
        pass


class GenericNode(TwiML):
    def __init__(self, name, value, **kwargs):
        super(GenericNode, self).__init__(**kwargs)
        self.name = name
        self.value = value
