import unittest
import time

from tempfile import NamedTemporaryFile 
from jsonfig.contents import FileContents, IntervalReloadFileContents

class TestFileContents(unittest.TestCase):
    def test_file_contents_are_loaded(self):
        with NamedTemporaryFile() as f:
            data = "yolo yolo yolo"
            data_md5 = "fd03e21c10f83acfed74f3ad832d3794"

            f.write(data)
            f.flush()
            
            fc = FileContents(f.name)
            self.assertEqual(data, fc.contents)
            self.assertEqual(data_md5, fc.hash_string)
        
    def test_file_contents_picked_up_on_reload(self):
        with NamedTemporaryFile() as f:
            data = "yolo yolo yolo"
            data_md5 = "fd03e21c10f83acfed74f3ad832d3794"

            f.write(data)
            f.flush()

            fc = FileContents(f.name)
            self.assertEqual(data, fc.contents)
            self.assertEqual(data_md5, fc.hash_string)

            data2 = "foo bar bim baz"
            data2_md5 = "b7752decac2d4475a3e87a4882768afc"

            f.seek(0)
            f.truncate()
            f.write(data2)
            f.flush()

            self.assertEqual(data, fc.contents)
            self.assertEqual(data_md5, fc.hash_string)

            fc.load()
            self.assertEqual(data2, fc.contents)
            self.assertEqual(data2_md5, fc.hash_string)

class TestIntervalReloadFileContents(unittest.TestCase):
    def test_file_contents_autoreload(self):
        with NamedTemporaryFile() as f:
            data = "yolo yolo yolo"
            data_md5 = "fd03e21c10f83acfed74f3ad832d3794"

            f.write(data)
            f.flush()

            fc = IntervalReloadFileContents(f.name, interval=1)
            self.assertEqual(data, fc.contents)
            self.assertEqual(data_md5, fc.hash_string)

            data2 = "foo bar bim baz"
            data2_md5 = "b7752decac2d4475a3e87a4882768afc"

            self.assertEqual(data, fc.contents)
            self.assertEqual(data_md5, fc.hash_string)

            # Have to sleep here to tick up the mtime
            time.sleep(1)

            f.seek(0)
            f.truncate()
            f.write(data2)
            f.flush()

            time.sleep(1)

            self.assertEqual(data2, fc.contents)
            self.assertEqual(data2_md5, fc.hash_string)

