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

class _UnixKeyReader:
    def __init__(self):
        import tty, sys, termios

    def __call__(self):
        import tty, sys, termios
        stdin_fd = sys.stdin.fileno()
        terminal_settings = termios.tcgetattr(stdin_fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            teernios