import os
import shutil
import tempfile
import errno


class ResourceProxy(object):
    def __init__(self):
        self._dir = tempfile.mkdtemp()

    def cleanup(self):
        try:
            shutil.rmtree(self._dir)  # delete directory
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

    def _file(self, file):
        return os.path.join(self._dir, file)

    def launch(self, *args, **kwargs):
        raise NotImplementedError

    def launch_unsafe(self, *args, **kwargs):
        raise NotImplementedError

    def __del__(self):
        self.cleanup()
