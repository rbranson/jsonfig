import unittest
import time

from tempfile import NamedTemporaryFile 
import jsonfig

class TestAPI(unittest.TestCase):
    def test_from_path_parses_json_into_dictionary(self):
        with NamedTemporaryFile() as f:
            f.write('{ "foo": "bar", "bim": "baz" }')
            f.flush()

            instance = jsonfig.from_path(f.name)
            self.assertEqual("bar", instance["foo"])
            self.assertEqual("baz", instance["bim"])

            # sleep here for the mtime rollover
            time.sleep(1)

            f.seek(0)
            f.truncate()
            f.write('{ "need": "there is none" }')
            f.flush()

            time.sleep(1)
            self.assertEqual("there is none", instance["need"])
            self.assertRaises(KeyError, lambda: instance["foo"])
            self.assertRaises(KeyError, lambda: instance["bim"])
         
    def test_from_path_doesnt_autoreload(self):
        pass

