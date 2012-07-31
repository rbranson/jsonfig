class ParseError(Exception):
    pass

class BaseFileContentsParser(object):
    """ Base class for parsing the contents of FileContents objects. Subclass
    and implement the :_parse: method, returning the parsed data structures.
    Only actually runs the :_parse: method if the file contents change."""

    def __init__(self, contents):
        self._contents = contents 
        self._last_hash = None
        self._parsed = None

    @property
    def parsed(self):
        """ Parsed data from the file contents provided. """

        # Try to only actually parse if the contents change
        if self._contents.hash_string != self._last_hash:
            self._parsed = self._parse(self._contents.contents)
            self._last_hash = self._contents.hash_string 

        return self._parsed

    def _parse(self, data):
        """ Subclassed method that parses the file contents """
        raise NotImplementedError()

class JsonFileContentsParser(BaseFileContentsParser):
    """ Parses JSON from a file. C'mon. Uses ujson if available.
    
    :param contents: The FileContents object containing the raw data.
    """
    
    def __init__(self, contents):
        super(JsonFileContentsParser, self).__init__(contents)

    def _parse(self, data):
        try:
            import ujson as json
        except:
            import json

        try:
            return json.loads(data)
        except ValueError, e:
            raise ParseError(e)

