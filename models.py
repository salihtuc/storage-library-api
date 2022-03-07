
class NotSupportedFormat(Exception):
    storage_format: str
    message: str

    def __init__(self, storage_format, message='This format is not supported by chosen destination.'):
        self.storage_format = storage_format
        self.message = message


class KeyNotFoundError(Exception):
    pass


class InvalidInputException(Exception):
    pass


class Record:
    name: str
    attrs: dict

    def __init__(self, name: str, attrs: dict):

        if name is None or attrs is None:
            raise InvalidInputException

        self.name = name
        self.attrs = attrs

    def __str__(self):
        return self.name + " -> " + str(self.attrs)

    def count(self):
        """This function returns the count of record's keys/attributes"""

        attrs = self.attrs
        return len(attrs)

    def insert(self, new_pairs: dict):
        """This function inserts key/value pairs to the record.
                Note that, if a key already in the record; it will be updated.
                So, it can be used as update operation.
                It returns"""

        if new_pairs is None:
            raise InvalidInputException

        attrs = self.attrs
        self.attrs = {**attrs, **new_pairs}

    def find_by_key(self, key: str):
        """This function returns the value of a key.
                    If the key is not in the record, it returns None."""

        if key is None or not isinstance(key, str):
            raise InvalidInputException

        attrs = self.attrs

        if key in attrs:
            return attrs[key]
        else:
            return None

    def find_pairs(self, pairs: dict):
        """This function returns a boolean value which indicates
                all of the given key/value pair(s) in the record or not."""

        if pairs is None:
            raise InvalidInputException

        return pairs.items() <= self.attrs.items()

    def update_by_key(self, key: str, new_val: str):
        """This function updates the value of a given key in record and returns the record.
                    If the key is not found, it raises KeyNotFoundError."""

        if key is None or new_val is None:
            raise InvalidInputException

        attrs = self.attrs

        if key not in attrs:
            raise KeyNotFoundError

        attrs[key] = new_val

        return self

    def delete_by_key(self, key: str):
        """This function deletes a given key and its value from record and returns the record.
                    If the key is not found, it raises KeyNotFoundError."""

        if key is None:
            raise InvalidInputException

        attrs = self.attrs

        if key not in attrs:
            raise KeyNotFoundError

        del attrs[key]

        return self
