from unittest import TestCase
from models import Record, InvalidInputException, KeyNotFoundError


class TestCreation(TestCase):
    def test_empty(self):
        self.assertRaises(Exception, lambda: Record())

    def test_none(self):
        self.assertRaises(InvalidInputException, lambda: Record(None, None))

    def test_regular(self):
        record = Record('sample', {})
        self.assertTrue(isinstance(record, Record))


class TestBaseOperations(TestCase):
    def setUp(self):
        self.record = Record('sample', {})

    def test_initial_count(self):
        self.assertEqual(self.record.count(), 0)

    def test_insert_one(self):
        self.record.insert({'key': 'value'})
        self.assertEqual(self.record.count(), 1)

    def test_insert_two(self):
        self.record.insert({'key1': 'value'})
        self.record.insert({'key2': 10})
        self.assertEqual(self.record.count(), 2)

    def test_find_by_none_key(self):
        self.assertRaises(InvalidInputException, lambda: self.record.find_by_key(None))

    def test_find_by_key(self):
        self.assertEqual(self.record.find_by_key('key'), None)

    def test_find_pairs_none(self):
        self.assertRaises(InvalidInputException, lambda: self.record.find_pairs(None))

    def test_find_pairs_empty(self):
        self.assertEqual(self.record.find_pairs({}), True)

    def test_find_pairs(self):
        self.assertEqual(self.record.find_pairs({'key': 'value'}), False)

    def test_update_by_none(self):
        self.assertRaises(InvalidInputException, lambda: self.record.update_by_key(None, None))

    def test_update_by_none_key(self):
        self.assertRaises(InvalidInputException, lambda: self.record.update_by_key(None, 'val'))

    def test_update_by_none_value(self):
        self.assertRaises(InvalidInputException, lambda: self.record.update_by_key('key', None))

    def test_update_by_key(self):
        self.assertRaises(KeyNotFoundError, lambda: self.record.update_by_key('key', 'val'))

    def test_delete_by_none_key(self):
        self.assertRaises(InvalidInputException, lambda: self.record.delete_by_key(None))

    def test_delete_by_key(self):
        self.assertRaises(KeyNotFoundError, lambda: self.record.delete_by_key('key'))


class TestOperationsWithData(TestCase):
    def setUp(self):
        self.record = Record('sample', {"key1": "val1", "key2": "val2"})

    def test_initial_count(self):
        self.assertEqual(self.record.count(), 2)

    def test_find_by_key(self):
        self.assertEqual(self.record.find_by_key('key1'), self.record.attrs['key1'])

    def test_find_pairs(self):
        self.assertEqual(self.record.find_pairs({'key1': 'val1'}), True)

    def test_update_by_key(self):
        rec_up = self.record.update_by_key('key1', 'newval1')

        self.assertEqual(rec_up.find_by_key('key1'), 'newval1')
        self.assertEqual(self.record.find_by_key('key1'), 'newval1')

    def test_delete_by_key(self):
        rec_del = self.record.delete_by_key('key1')

        self.assertEqual(rec_del.find_by_key('key1'), None)
        self.assertEqual(self.record.find_by_key('key'), None)
