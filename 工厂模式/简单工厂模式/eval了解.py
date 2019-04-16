class Por(object):
    def cal(self, x, y):
        return x + y


def ccal(x, y):
    return x + y


if __name__ == '__main__':
    a = eval('ccal')(3,6)
    print(a)
