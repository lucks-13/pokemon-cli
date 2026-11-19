class _keyReader:
    def __init__(self):
        try:
            self.key_reader = _WindowsKeyReader()
        except ImportError:
            try:
                self.key_reader = _MacKeyReader()
            except (AttributeError, ImportError):
                self.key_reader = _UnixKeyReader()

    def __call__(self):
        return self.key_reader()

