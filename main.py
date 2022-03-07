from models import Record
from destinations import FileDestination
from formats import JsonFormat


if __name__ == '__main__':

    """Simple demo: FileDestination and Json format"""

    some_dict = {'a': 5, 'b': '4'}

    record = Record('sample', some_dict)
    dest = FileDestination()
    json_format = JsonFormat()

    record.insert({"a": 55, "c": 14, "d": 'value'})

    stored_file = dest.store(record, json_format)

    print('{} stored in file system.'.format(stored_file))

    parsed_text = dest.parse(stored_file, json_format)
    print('\nContent:')
    print(parsed_text)

