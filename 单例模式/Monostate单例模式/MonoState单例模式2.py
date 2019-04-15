class Borg():
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


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
