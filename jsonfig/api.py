from jsonfig.contents import IntervalReloadFileContents
from jsonfig.parse import JsonFileContentsParser
from jsonfig.util import DictionaryProxy

def from_path(path, autoreload=True, autoreload_interval=1.0):
    """ Returns a dictionary that loads it's contents from a JSON file,
    specified by the :path: argument. Periodically it will check to see if the
    contents of the file have changed and reload it.

    :param path: The file containing the JSON data.
    :keyword autoreload: Turns on periodic checks of the file for new data.
    :keyword autoreload_interval: How often (in seconds) to check the file for
    changes."""

    if autoreload is True: 
        contents = IntervalReloadFileContents(path, interval = autoreload_interval)
    else:
        contents = FileContents(path)

    parser = JsonFileContentsParser(contents)
    return DictionaryProxy(lambda: parser.parsed)
