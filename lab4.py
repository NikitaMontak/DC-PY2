import doctest

class Accelerator:

    """ Базовый класс, описывающий ускоритель заряженных частиц """

    max_energy = 1000

    def __init__(self, particle: str, energy: int):
        """
        Инициализация экземпляра класса Ускоритель
        :param particle: тип ускоряемой частицы
        :param energy: энергия в МэВ/нуклон, до которой частица ускоряется

        Пример:
        >>> accelerator_1 = Accelerator('proton', 80)"""

        if not isinstance(particle, str):
            raise TypeError("Частица должна быть типа str")

        if not isinstance(energy, int):
            raise TypeError("Энергия должна быть типа int")

        if energy > Accelerator.max_energy:
            raise ValueError("Энергия превышает допустимое значение")

        if energy <= 0:
            raise ValueError("Энергия не может быть отрицательной")

        self.particle = particle
        self.energy = energy
        self._purpose = None  # Назначение ускорителя. По умолчанию отсутствует, добавляется методом add_purpose
        self._country = None  # Страна разработки ускорителя. По умолчанию отсутствует, добавляется методом add_country

    def __str__(self) -> str:
        return f"Ускоряемая частица: {self.particle}, энергия ускорения: {self.energy}"

    def __repr__(self) -> str:
        return f"particle({self.particle!r}), energy({self.energy})"

    def change_energy(self, new_energy: int) -> None:
        """
           Метод, позволяющий изменить энергию частицы
           :param new_energy: новое значение энергии
           :return:

           Пример:
           >>> accelerator_1 = Accelerator('proton', 80)
           >>> accelerator_1.change_energy(200)
           """

        if new_energy > Accelerator.max_energy:
            raise ValueError("Энергия превышает допустимое значение")

        if new_energy <= 0:
            raise ValueError("Энергия не может быть отрицательной")

        self.energy = new_energy

    def add_purpose(self, purpose: str) -> None:
        """
        Метод, позволяющий добавить назначение ускорителя
        :param purpose: назначение
        :return:

        Пример:
        >>> accelerator_1 = Accelerator('proton', 80)
        >>> accelerator_1.add_purpose("медицинский")
        """

        if not isinstance(purpose, str):
            raise TypeError("Назначение должно быть типа str")

        self._purpose = purpose

    def add_country(self, country: str) -> None:
        """
        Метод, позволяющий добавить страну разработки
        :param country: название страны
        :return:

        Пример:
        >>> accelerator_1 = Accelerator('proton', 80)
        >>> accelerator_1.add_country("Россия")
        """

        if not isinstance(country, str):
            raise TypeError("Название страны должно быть типа str")

        self._country = country

    def get_country(self) -> str:
        """
        Метод, возвращающий название страны-разработчика ускорителя
        :return: название страны

        Пример:
        >>> accelerator_1 = Accelerator('proton', 80)
        >>> accelerator_1.add_country("Россия")
        >>> accelerator_1.get_country()
        'Россия'
        """

        return self._country


class Cyclotron(Accelerator):

    """Дочерний класс для класса Ускорители"""

    max_radius = 5.0

    def __init__(self, particle: str, energy: int, type: str, radius: float):
        """
        Инициализация экземпляра класса Циклотрон
        :param particle: тип ускоряемой частицы
        :param energy: энергия в МэВ/нуклон, до которой ускоряется частица
        :param type: тип циклотрона
        :param radius: радиус циклотрона в метрах

        Пример:
        >>> cyclotron_1 = Cyclotron('Bi', 100, 'изохронный', 2.2)
        """

        if not isinstance(type, str):
            raise TypeError("Тип циклотрона должен быть типа str")

        if not isinstance(radius,float):
            raise TypeError("Радиус циклотрона должен быть типа float")

        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")

        if radius > Cyclotron.max_radius:
            raise ValueError("Указанный радиус превышает допустимое значение")

        super().__init__(particle, energy)
        self.type = type
        self.radius = radius
        self._purpose = None
        self._country = None

    def __str__(self) -> str:  # Перегрузка __str__ и __repr__ необходима, так как в дочерний класс добавляются параметры
        return f"Ускоряемая частица: {self.particle}, энергия ускорения: {self.energy}, тип ускорителя: циклотрон {self.type}, радиус: {self.radius}"

    def __repr__(self) -> str:
        return f"particle({self.particle!r}), energy({self.energy}), type({self.type!r}), radius({self.radius})"


if __name__ == "__main__":
    pass
    doctest.testmod()
