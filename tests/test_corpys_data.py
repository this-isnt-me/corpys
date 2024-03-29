import unittest
import uuid
from corpys.corpys_data import CorpysData

lorum_ipsum_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

class TestCorpysData(unittest.TestCase):
    def test_sent_id_attribute(self):
        obj = CorpysData(lorum_ipsum_string)
        # Check if the attribute exists
        self.assertTrue(hasattr(obj, 'sent_id'))
        # Check if the attribute is a string
        self.assertIsInstance(obj.sent_id, str)

    def test_text_attribute(self):
        obj = CorpysData(lorum_ipsum_string)
        # Check if the attribute exists
        self.assertTrue(hasattr(obj, 'text'))
        # Check if the attribute is a string
        self.assertIsInstance(obj.text, str)
