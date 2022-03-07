import json
import xmltodict
from abc import ABC, abstractmethod


class Format(ABC):

    extension: str

    @abstractmethod
    def to_format(self, attrs):
        pass

    @abstractmethod
    def from_format(self, formatted: str):
        pass


class JsonFormat(Format):

    extension = 'json'

    def to_format(self, attrs):
        return json.dumps(attrs, indent=4)

    def from_format(self, formatted: str):
        return json.loads(formatted)


class XMLFormat(Format):

    extension = 'xml'
    __additional_keyword = 'records'

    def to_format(self, attrs):
        modified_attrs = {self.__additional_keyword: attrs}
        return xmltodict.unparse(modified_attrs, pretty=True)

    def from_format(self, formatted: str):
        parsed = xmltodict.parse(formatted)
        if self.__additional_keyword in parsed:
            return parsed[self.__additional_keyword]
