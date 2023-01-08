import doctest


# TODO Написать 3 класса с документацией и аннотацией типов


class Kettle:

    def __init__(self, volume: float, temp: int, power: int):
        """
        Создание объекта класса "Чайник"
        :param volume: объём воды в чайнике в литрах
        :param temp: температура воды в чайнике в С
        :param power: мощность чайника в Вт

        Пример:
        >>> my_Kettle = Kettle(2.0, 80, 1500)
        """

        if not isinstance(volume, float):
            raise TypeError("Объем должен быть типа float")
        if volume <= 0:
            raise ValueError("Объём должен быть положительным")
        if not isinstance(temp, int):
            raise TypeError("Температура должна быть типа int")
        if temp <= 0:
            raise ValueError("Температура должна быть положительной")
        if not isinstance(power, int):
            raise TypeError("Мощность должна быть типа int")
        if power <= 0:
            raise ValueError("Мощность должна быть положительной")
        self.volume = volume
        self.temp = temp
        self.power = power

    def set_temp(self, new_temp: float) -> None:
        """Функция задаёт новую температуру для чайника.

        Пример:
        >>> my_Kettle = Kettle(2.0,80,1500)
        >>> my_Kettle.set_temp(10)
        """

        self.temp = new_temp
        ...

    def set_volume(self, new_volume: float) -> None:
        """Функция задаёт новый объёсм воды в чайнике.

        Пример:
        >>> my_Kettle = Kettle(2.0,80,1500)
        >>> my_Kettle.set_volume(1.5)
        """
        self.volume = new_volume
        ...

    def boil(self) -> None:
        """Функция кипятит воду в чайнике.

        Пример:
        >>> my_Kettle = Kettle(2.0,80,1500)
        >>> my_Kettle.boil()
        """
        ...


class Cat:
    def __init__(self, name: str, color: str, age: int):
        """
        Создание объекта класса "Кошка"
        :param name: имя кошки
        :param color: окрас
        :param age: возраст

        Пример:
        >>> cat_1 = Cat('Barsik', 'black', 2)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет должен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст должен быть положительным")

        self.name = name
        self.color = color
        self.age = age

    def sleep(self, time: float) -> None:
        """Функция задаёт количество часов, которое спит кошка.
        :param time: время сна

        Пример:
        >>> cat_1 = Cat('Barsik', 'black', 2)
        >>> cat_1.sleep(8)
        """
        ...

    def eat(self, food: str, mass: float) -> None:
        """Функция задаёт количество и вид корма для кошки
        :param food: вид корма
        :param mass: масса корма в граммах
        :raise TypeError: ошибка, если тип корма задаётся не строкой
        :raise ValueError: ошибка, если объём корма отрицательный

        Пример:
        >>> cat_1 = Cat('Barsik', 'black', 2)
        >>> cat_1.eat('meat', 200)
        """
        ...


class Cake:
    def __init__(self, mass: float, shape: str, date: int):
        """Создание объекта класса "Торт".
        :param mass: масса торта в кг
        :param shape: форма торта
        :param date: срок годности в днях

        Пример:
        >>> smetannik = Cake(2.5, 'circle', 5)
        """
        if not isinstance(mass, float):
            raise TypeError("Масса должна иметь тип float")
        if mass < 0:
            raise ValueError("Масса должна быть положительной")
        if not isinstance(shape, str):
            raise TypeError("Фома должна иметь тип str")
        if not isinstance(date, int):
            raise TypeError("Срок должен быть типа int")
        if date < 0:
            raise ValueError("Срок годности должен быть положительным")
        self.mass = mass
        self.shape = shape
        self.date = date

    def cut(self, number_of_pieceses: int) -> None:
        """Функция разрезает торт на количество кусочков, заданное пользователем
        :param number_of_pieceses: количество кусочков
        :raise TypeError: если число кусочков не целое

        Пример:
        >>> smetannik = Cake(2.5, 'circle', 5)
        >>> smetannik.cut(10)
        """
        ...

    def throw_out(self, number_of_days: int) -> bool:
        """Функция сравнивает срок годности торта со сроком хранения, заданным пользователем.
        :param number_of_days: число дней, которое хранится торт
        :return True: если number_of_days <= date, иначе
        :return False

        Пример:
        >>> smetannik = Cake(2.5, 'circle', 5)
        >>> smetannik.throw_out(3)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
