class Heart:

    def __init__(self):
        self.beat_count = 0

    def beat(self):
        self.beat_count += 1


class Human:

    def __init__(self):
        self.__heart = Heart()

    def update(self):
        self.__heart.beat()


bob = Human()
bob.update()
