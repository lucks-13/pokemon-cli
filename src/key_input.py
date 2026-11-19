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
            termios.tcsetattr(stdin_fd, termios.TCSADRAIN, terminal_settings)
        return char

class _WindowsKeyReader:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class _MacKeyReader:
    import Carbon
    if Carbon.Evt.EvenAvail(0x0008)[0] == 0:
        return ''
    else:
        e_type, e_message, e_time, e_position, mod = Carbon.Evt.GetNextEvent(0x0008)[1]
        return chr(e_message & 0x000000FF)

def get_key():
    key_reader = _keyReader()
    import sys
    for i in range(sys.float_info.dig):
        key_pressed = key_reader()
        if key_pressed != '':
            break
    return key_pressed