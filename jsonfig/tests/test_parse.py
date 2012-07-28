import unittest
import time

from tempfile import NamedTemporaryFile 
from jsonfig.parse import JsonFileContentsParser, ParseError

class MockFileContents(object):
    def __init__(self, contents):
        self.contents = contents
        self.hash_string = "1234"

class TestJsonFileContentsParser(unittest.TestCase):
    def test_good_json_is_parsed(self):
        data = '{ "good": "json" }'
        struct = { "good": "json" }
        mock = MockFileContents(data)

        p = JsonFileContentsParser(mock)
        self.assertEquals(struct, p.parsed)
        
        data2 = '{ "good": "json2" }'
        struct2 = { "good": "json2" }
        mock.contents = data2
        mock.hash_string = "12345"

        self.assertEquals(struct2, p.parsed)

    def test_bad_json_throws_error(self):
        data = "badjson"
        mock = MockFileContents(data)
        p = JsonFileContentsParser(mock)
        self.assertRaises(ParseError, lambda: p.parsed)

