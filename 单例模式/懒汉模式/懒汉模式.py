class Singletion():
    __instance = None

    def __init__(self):
        if not Singletion.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singletion()
        return cls.__instance


if __name__ == '__main__':
    s = Singletion()
    print("Object created", Singletion.getInstance())
    s1 = Singletion()
