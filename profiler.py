import datetime

class Profiler:
    def __init__(self):
        self.startTime = datetime.datetime.now()

    def get_seconds(self):
        endTime = datetime.datetime.now()
        diff = endTime - self.startTime
        return diff.total_seconds()
