# Инкапсуляция часть 2

class Test:
    def public_function(self):
        print("Публичный метод")

    def _protected_function(self):
        print("Защищенный метод")

    def __private_function(self):
        print("Приватный метод")

    def test_private(self):
        self.__private_function()

    def test_protected(self):
        self._protected_function()



test = Test()
test.public_function()
test.test_protected()
test.test_private()
