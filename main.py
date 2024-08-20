# Домашнее задание:

import pickle

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, level):
        if level in ['user', 'admin']:
            self._access_level = level
        else:
            raise ValueError("Неверный уровень доступа")

    def __repr__(self):
        return f"User(ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.set_access_level('admin')

    def add_user(self, user_list, user):
        if user.get_user_id() == 1:
            print("Нельзя добавить пользователя с ID 1, так как он зарезервирован для администратора.")
            return

        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Неверный объект пользователя.")

    def remove_user(self, user_list, user_id):
        if user_id == 1:
            print("Нельзя удалить администратора.")
            return

        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удалён.")
                return
        print("Пользователь не найден.")

    def update_user(self, user_list, user_id, new_name):
        if user_id == 1:
            print("Нельзя обновить данные администратора.")
            return

        for user in user_list:
            if user.get_user_id() == user_id:
                user.set_name(new_name)
                print(f"Пользователь {user.get_name()} обновлён.")
                return
        print("Пользователь не найден.")

    def __repr__(self):
        return f"Admin(ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level})"


def save_users(user_list, filename='users.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(user_list, file)
    print("Учетные записи сохранены.")


def load_users(filename='users.pkl'):
    try:
        with open(filename, 'rb') as file:
            user_list = pickle.load(file)
        print("Учетные записи загружены.")
        return user_list
    except FileNotFoundError:
        print("Файл учетных записей не найден. Создан пустой список.")
        return []


def main():
    user_list = load_users()
    admin = Admin(user_id=1, name="Администратор")

    while True:
        print("\n1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Обновить пользователя")
        print("4. Список пользователей")
        print("5. Сохранить и выйти")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            user_id = int(input("Введите ID пользователя: "))
            name = input("Введите имя пользователя: ")
            user = User(user_id=user_id, name=name)
            admin.add_user(user_list, user)

        elif choice == '2':
            user_id = int(input("Введите ID пользователя для удаления: "))
            admin.remove_user(user_list, user_id)

        elif choice == '3':
            user_id = int(input("Введите ID пользователя для обновления: "))
            new_name = input("Введите новое имя пользователя: ")
            admin.update_user(user_list, user_id, new_name)

        elif choice == '4':
            for user in user_list:
                print(user)

        elif choice == '5':
            save_users(user_list)
            print("Завершение программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()