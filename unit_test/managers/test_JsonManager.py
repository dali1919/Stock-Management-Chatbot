import json
import logging

from unittest import TestCase, TestSuite, TextTestRunner
from managers import JsonManager


class TestJsonManager(TestCase):
    def test_validate_json(self):
        str_json = '{"key1":"value1", "key2":3}'
        json_obj = json.loads(str_json)
        self.assertTrue(JsonManager.JsonManager.validate_json(str_json))
    def test_serialize_dict(self):
        dict_obj = {'key1': 'value1', 'key2': 'value2'}
        json_obj = json.dumps(dict_obj)
        json_obj = json_obj.replace("'", '\\"')
        self.assertEqual(json_obj, JsonManager.JsonManager.serialize_dict(dict_obj))

    def test_deserialize_dict(self):
        dict_obj = {'key1': 'value1', 'key2': 'value2'}
        json_data = json.dumps(dict_obj)
        self.assertEqual(dict_obj, JsonManager.JsonManager.deserialize_dict(json_data))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    test_suite = TestSuite()
    test_suite.addTest(TestJsonManager('test_validate_json'))
    test_suite.addTest(TestJsonManager('test_serialize_dict'))
    test_suite.addTest(TestJsonManager('test_deserialize_dict'))
    TextTestRunner(verbosity=2).run(test_suite)