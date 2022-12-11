# TODO Написать 3 класса с документацией и аннотацией типов


class Kettle:
    def __init__(self, volume: float, temp: float, power: int):
        if not isinstance(temp, float):
            raise TypeError("Температура должна быть типа float")
        if not isinstance(volume, float):
            raise TypeError("Объем должен быть типа float")
        if not isinstance(power, int):
            raise TypeError("Мощность должна быть типа int")
        self.volume = volume  # объем, л
        self.temp = temp  # температура, С
        self.power = power  # мощность, Вт

    def set_temp(self, new_temp: float) -> None:
        self.temp = new_temp
        ...

    def set_volume(self, new_volume: float) -> None:
        self.volume = new_volume
        ...

    def boil(self) -> None:
        """Кипятит воду"""
        ...


class Cat:
    def __init__(self, name: str, color: str, age: int):
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет должен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        self.name = name
        self.color = color
        self.age = age

    def sleep(self, time: float) -> None:
        """спит time часов"""
        ...

    def eat(self, food: str, volume: float) -> None:
        """ест volume корма food"""
        ...

class Cake:
    def __init__(self, mass: float, shape: str, date: int):
        if not isinstance(mass, float):
            raise TypeError("Масса должна иметь тип float")
        if not isinstance(shape, str):
            raise TypeError("Фома должна иметь тип str")
        if not isinstance(date, int):
            raise TypeError("Срок должен быть типа int")
        self.mass = mass
        self.shape = shape
        self.date = date  # срок годности

    def cut(self, number_of_pieceses: int) -> None:
        """порезать на кусочки"""
        if not isinstance(number_of_pieceses, int):
            raise TypeError("Число кусочков должно быть целым")
        ...

    def throw_out(self, date, number_of_days: int) -> bool:
        """проверить срок годности"""
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
