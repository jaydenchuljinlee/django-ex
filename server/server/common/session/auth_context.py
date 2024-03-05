import threading


class SingletonThreadLocal(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class ThreadLocalSingleton(metaclass=SingletonThreadLocal):
    def __init__(self):
        self.thread_local_data = threading.local()

    def set_data(self, data):
        self.thread_local_data.data = data

    def get_data(self):
        return getattr(self.thread_local_data, 'data', None)

