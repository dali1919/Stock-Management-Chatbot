"""
Provides json related utilities like validation, serialization/deserialization, etc.

"""
import json
import logging


class JsonManager:

    @staticmethod
    def validate_json(str_json):
        """
        Method takes in an object and validates if it is valid JSON or not.
        :rtype: Boolean: True if json is valid, False otherwise
        """
        try:
            json.loads(str_json)
            return True
        except ValueError as error:
            logging.error("Invalid JSON: {}".format(error))
            return False

    @staticmethod
    def serialize_dict(dict_object):
        """
        Method to serialize python dictionary for storage into DBs.
        :rtype: serialized dictionary
        """
        if not dict_object:
            logging.error("DICTIONARY NOT SERIALIZABLE: {}".format(dict_object))
        else:
            return json.dumps(dict_object).replace("'", '\\"').replace("False","false").replace("True", "true")

    @staticmethod
    def deserialize_dict(obj):
        """
        Method to deserialize object to get back python dictionary.
        :rtype: python dictionary corresponding to serialized object
        """
        if not obj:
            logging.error("OBJECT NOT DESERIALIZABLE: {}".format(obj))
        else:
            return json.loads(obj)
