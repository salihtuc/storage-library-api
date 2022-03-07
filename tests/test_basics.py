from unittest import TestCase
from models import Record
from destinations import FileDestination, S3Destination
from formats import JsonFormat, XMLFormat


class TestBasicsJsonFile(TestCase):
    def setUp(self):
        some_dict = {'a': 5, 'b': '4'}
        self.record = Record('sample', some_dict)
        self.dest = FileDestination()
        self.json_format = JsonFormat()

    def test_simple_operation(self):

        record_name = self.dest.store(self.record, self.json_format)

        self.assertEqual(record_name, self.record.name)

        record_obj = self.dest.parse(record_name, self.json_format)

        self.assertTrue(self.record.attrs, record_obj.attrs)


class TestBasicsXMLFile(TestCase):
    def setUp(self):
        some_dict = {'a': 5, 'b': '4'}
        self.record = Record('sample', some_dict)
        self.dest = FileDestination()
        self.xml_format = XMLFormat()

    def test_simple_operation(self):

        record_name = self.dest.store(self.record, self.xml_format)

        self.assertEqual(record_name, self.record.name)

        record_obj = self.dest.parse(record_name, self.xml_format)

        self.assertTrue(self.record.attrs, record_obj.attrs)


class TestBasicsJsonS3(TestCase):
    def setUp(self):
        some_dict = {'a': 5, 'b': '4'}
        self.record = Record('sample', some_dict)
        self.dest = S3Destination('<aws_key>', '<aws_secret>', '<bucket_name>')
        self.json_format = JsonFormat()

    def test_simple_operation(self):

        record_name = self.dest.store(self.record, self.json_format)

        self.assertEqual(record_name, self.record.name)

        record_obj = self.dest.parse(record_name, self.json_format)

        self.assertTrue(self.record.attrs, record_obj.attrs)


class TestBasicsXMLS3(TestCase):
    def setUp(self):
        some_dict = {'a': 5, 'b': '4'}
        self.record = Record('sample', some_dict)
        self.dest = S3Destination('<aws_key>', '<aws_secret>', '<bucket_name>')
        self.xml_format = XMLFormat()

    def test_simple_operation(self):

        record_name = self.dest.store(self.record, self.xml_format)

        self.assertEqual(record_name, self.record.name)

        record_obj = self.dest.parse(record_name, self.xml_format)

        self.assertTrue(self.record.attrs, record_obj.attrs)
