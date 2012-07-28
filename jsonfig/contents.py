import time
import os
import hashlib

class FileContents(object):
    """Loads the contents of a file and holds it in memory.
    
    :param path: Path to the file to load 
    """

    def __init__(self, path):
        self._path = path
        self._contents = None
        self._hash = None

        self.load()

    def load(self):
        """ Refreshes the contents of the file. """
        with open(self._path, "r") as f:
            self._contents = f.read() 
            self._hash = self._hash_string_from_string(self._contents)

    @property
    def contents(self):
        """ Returns the file contents. """
        return self._contents 

    @property
    def hash_string(self):
        """ Returns a string that contains a hash for the loaded file contents. """
        return self._hash

    def _hash_string_from_string(self, s):
        return hashlib.md5(s).hexdigest() 

class IntervalReloadFileContents(FileContents):
    """Loads the contents of a file and holds it in memory. Each time the
    file contents are requested, checks to see if the file has been modified
    since last checked.
    
    :param path: Path to the file to load.
    :keyword interval: The interval (in seconds) between modification checks.
    """

    def __init__(self, path, interval = 1):
        self._last_check = 0
        self._last_mtime = 0
        self._interval = interval

        super(IntervalReloadFileContents, self).__init__(path)

    @property
    def contents(self):
        """ Returns the file contents. """
        self._check_reload()
        return super(IntervalReloadFileContents, self).contents
    
    @property
    def hash_string(self):
        """ Returns a string that contains a hash for the loaded file contents. """
        self._check_reload()
        return super(IntervalReloadFileContents, self).hash_string

    def _check_reload(self):
        ctime = time.time()

        if ctime >= self._last_check + self._interval:
            stat = os.stat(self._path)

            if stat.st_mtime != self._last_mtime:
                self.load() 
                self._last_mtime = stat.st_mtime

            self._last_check = ctime
