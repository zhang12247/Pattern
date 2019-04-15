class Borg:
    _shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self._shared_state
        pass


if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4
    b2 = Borg()

    print("Borg Object 'b':", b)
    print("Borg Object 'b1':", b1)
    print("objcet state 'b':", b.__dict__)
    print("object state 'b1':", b1.__dict__)
    print("object state 'b2':", b2.__dict__)
