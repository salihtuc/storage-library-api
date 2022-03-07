from abc import ABC, abstractmethod
from models import Record
from formats import Format
from os import path
import utils
import boto3


class Destination(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'store') and
                callable(subclass.store) and
                hasattr(subclass, 'parse') and
                callable(subclass.parse) or
                NotImplemented)

    @abstractmethod
    def store(self, record: Record, storage_format: Format):
        """This function stores the record to the destination"""
        pass

    @abstractmethod
    def parse(self, record_name: str, storage_format: Format):
        """THis function returns a record from the destination"""
        pass


class FileDestination(Destination):

    def __init__(self, base_path='storage'):
        self.base_path = base_path

    def store(self, record: Record, storage_format: Format):
        if record is None or record.name is None or record.attrs is None:
            raise Exception

        # Check the local directory for the base_path
        utils.check_and_fix_directory(self.base_path)

        # Organize the file name and join it with base_path
        file_name = record.name + '.' + storage_format.extension
        full_path = path.join(self.base_path, file_name)

        # Prepare the file pointer for writing
        fp = open(full_path, 'w+')

        # Create formatted string from the dict
        formatted = storage_format.to_format(record.attrs)

        # Write & Save the content into the file
        fp.write(formatted)
        fp.close()

        return record.name

    def parse(self, record_name: str, storage_format: Format):

        # Organize the file name and join it with base_path
        file_name = record_name + '.' + storage_format.extension
        full_path = path.join(self.base_path, file_name)

        # Prepare the file pointer for reading
        fp = open(full_path, 'r+')

        # Read the file content into a string
        formatted = fp.read()

        fp.close()

        # Create a dict from formatted string of chosen Format
        attrs = storage_format.from_format(formatted)

        # Create and return the Record object
        return Record(record_name, attrs)


class S3Destination(Destination):

    def __init__(self, aws_key, aws_secret, bucket, base_path='storage'):

        # It may move to outside (and the session can get as parameter)
        session = boto3.Session(
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret
        )

        # Get the S3 resource and other attributes
        self.resource = session.resource('s3')
        self.bucket = bucket
        self.base_path = base_path

    def store(self, record: Record, storage_format: Format):
        if record is None or record.name is None or record.attrs is None:
            raise Exception

        # Create file name and join it with base_path
        file_name = record.name + '.' + storage_format.extension
        full_path = path.join(self.base_path, file_name)

        # Create s3 object
        s3_object = self.resource.Object(self.bucket, full_path)

        # Get the formatted string of the chosen Format
        formatted = storage_format.to_format(record.attrs)

        # Put the object to the S3 (as byte string)
        result = s3_object.put(Body=str(formatted).encode('utf-8'))

        # Get the result data
        res = result.get('ResponseMetadata')

        # If operation is OK, return the record, None otherwise
        if res.get('HTTPStatusCode') == 200:
            return record.name
        else:
            print('File Not Uploaded')
            return None

    def parse(self, record_name: str, storage_format: Format):

        # Create file name and join it with base_path
        file_name = record_name + '.' + storage_format.extension
        full_path = path.join(self.base_path, file_name)

        # Create s3 object
        s3_object = self.resource.Object(self.bucket, full_path)

        # Get the file content from S3
        file_content = s3_object.get()['Body'].read().decode('utf-8')

        # Parse the content by chosen Format
        attrs = storage_format.from_format(file_content)

        # Return the Record object
        return Record(record_name, attrs)
