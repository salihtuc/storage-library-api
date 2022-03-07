from models import Record
from destinations import FileDestination
from formats import JsonFormat


if __name__ == '__main__':

    """Simple demo: FileDestination and Json format"""

    # Create a sample dict
    some_dict = {'a': 5, 'b': '4'}

    # Create a sample record
    record = Record('sample', some_dict)

    # Call Custom destination
    destination = FileDestination()
    json_format = JsonFormat()

    # Custom record operations
    record.insert({"a": 55, "c": 14, "d": 'value'})

    # Store the record
    stored_file = destination.store(record, json_format)

    print('{} stored in file system.'.format(stored_file))

    # Get the record from stored file
    record_from_system = destination.parse(stored_file, json_format)
    print('\nContent:')
    print(record_from_system)

