# There is now a separate copy of profiler.py for each subfolder, so you can run Python files in those subfolders
# directly from their own folders rather than having to have the parent folder as the current working directory

import time

class Profiler:
    def __init__(self, name=""):
        self.start_time = time.perf_counter()
        self.name = name

    def get_ms(self):
        return self.get_seconds() * 1000

    def get_seconds(self):
        endTime = time.perf_counter()
        diff = endTime - self.start_time
        return diff

    def __str__(self):
        return "{0}: {1}ms".format(self.name, self.get_ms())