class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        # self.name = name
        # self.author = author
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        # Проверка, что число страниц целое и больше нуля
        if isinstance(value, int):
            if value > 0:
                self.pages = value
            else:
                raise ValueError(f'Должна быть хотя бы одна страница! Текущее значение: {value!r}')
        else:
            raise ValueError(f'Число страниц должно быть целым! Текущее значение: {value!r}')

    def __str__(self):
        # наследование параметров базового класса
        tmp_str = super.__str__(self)
        # добавление атрибута для класса бумажной книги
        return f"{tmp_str}. Число страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self.pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        # self.name = name
        # self.author = author
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        # Проверка, что длительность - число типа float больше нуля
        if isinstance(value, float):
            if value > 0:
                self._duration = value
            else:
                raise ValueError(f'Длительность должна быть положительной! Текущее значение: {value!r}')
        else:
            raise ValueError(f'Длительность должна быть типа float! Текущее значение: {value!r}')

    def __str__(self):
        # Наследование атрибутов базового класса и добавление нового атрибута
        tmp_str = super.__str__(self)
        return f"{tmp_str}. Длительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, duration = {self.duration}"
