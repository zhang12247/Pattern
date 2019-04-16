from abc import ABC, abstractmethod


# 构建父类 披萨工厂
class PizzaFactory(ABC):
    # 构建虚方法生产蔬菜披萨，需要被继承
    @abstractmethod
    def createVegPizza(self):
        pass

    # 构建虚方法生产非蔬菜披萨，需要被继承
    @abstractmethod
    def createNonVegPizza(self):
        pass


#印第安披萨工厂继承披萨工厂
class IndianPizzaFactory(PizzaFactory):
    #实现创建蔬菜披萨
    def createVegPizza(self):
        return DeluxVeggiePizza()

    # 实现创建非蔬菜披萨
    def createNonVegPizza(self):
        return ChickenPizza()

#USP披萨工厂继承披萨工厂
class USPizzaFactory(PizzaFactory):
    # 实现创建蔬菜披萨
    def createVegPizza(self):
        return MexicanVegPizza()

    # 实现创建非蔬菜披萨
    def createNonVegPizza(self):
        return HamPizza()


#素食披萨父类
class VegPizza(ABC):
    #抽象方法需要被继承
    @abstractmethod
    def prepare(self, VegPizza):
        pass

#非素食披萨父类
class NonVegPizza(ABC):
    #抽象方法需要被继承
    @abstractmethod
    def serve(self, VegPizza):
        pass


#Delux继承素食披萨，进行准备
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

#鸡肉皮塞继承非素食披萨，进行加料
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class PizzaStord:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


if __name__ == '__main__':
    pizza = PizzaStord()
    pizza.makePizzas()
