import time
import io

class LooseLogs:
    def __init__(self, path, writer, buffer_size=4096):
        self.logs_strong_path = path
        self.logs_writer = writer
        self.buffer_size = buffer_size
        self.logs_object = None
        self.is_initialized = False

    def check_logs_initialized(func):
        def wrapper(self, *args):
            if self.is_initialized:
                return func(self, *args)
            else:
                raise Exception("The logs is not initialized!\
                    \n\t   Add \"self.initialize_logs()\" in your code.\
                    \n\t   Otherwise we cannot keep your code running smoothly.")
        return wrapper

    def initialize_logs(self):
        self.logs_object = io.open(self.logs_strong_path, "a", buffering=self.buffer_size)
        self.is_initialized = True

    @check_logs_initialized
    def write_log(self, level, info):
        try:
            write_text = self._format_time() + f"-{self.logs_writer}-[{level}] - {info}\n"
            self.logs_object.write(write_text)
            self.logs_object.flush()
            return 0, None
        except Exception as ex:
            return 1, ex

    @check_logs_initialized
    def write_logs(self, level, info):
        try:
            write_text = self._format_time() + f"-{self.logs_writer}-[{level}] # ----------------------------------------\n"
            self.logs_object.write(write_text)
            for log in info:
                write_text = self._format_time() + f"-{self.logs_writer}-[{level}] | {log}\n"
                self.logs_object.write(write_text)
            write_text = self._format_time() + f"-{self.logs_writer}-[{level}] # ----------------------------------------\n"
            self.logs_object.write(write_text)
            self.logs_object.flush()
            return 0, None
        except Exception as ex:
            return 1, ex

    def _format_time(self):
        return time.strftime("(%Y/%m/%d %H:%M:%S)", time.localtime())