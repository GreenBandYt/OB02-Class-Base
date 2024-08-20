# Инкапсуляция

class Test:
    def __init__(self):
        self.pablic = "публичное"
        self._protected = "защищенное"
        self.__private = "приватное"

    def test(self):
        print(self.pablic)
        print(self._protected)
        print(self.__private)
    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value

test = Test()

print(test.pablic)
print(test._protected)
print(test.get_private())

test.set_private("приватное значение")
print(test.get_private())

