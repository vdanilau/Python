class Hero():
    """ Class to create Hero for game """

    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """" Print all parameters of this Hero """
        description = (self.name + ": Level is:" + str(self.level) + "; Race is: " + self.race + "; Health is:" + str(
            self.health)).title()
        print(description)

    def level_up(self):
        """ Upgrade level """
        self.level += 1

    def move(self):
        """ Start moving of Hero """
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """ Class to create Super Hero """

    def __init__(self, name, level, race, magiclevel):
        """ Initiate super Hero"""
        super().__init__(name, level, race)  # Оъявление суперкласса (родителя)
        self.magiclevel = magiclevel
        self.__magic = 100  # запрет доступа к полю из вне класса. Без этого можно сделать в main просто myherp.magic = 10 и 10 присвоится

    def make_magik(self):
        """ Use magic """
        self.__magic -= 10

    def show_hero(self):
        """" Print all parameters of this Hero """
        description = (self.name +
                       ": Level is:" + str(self.level) +
                       "; Race is:" + self.race +
                       "; Health is:" + str(self.health) +
                       "; Magic is:" + str(self.__magic) +
                       "; Magic level is:" + str(self.magiclevel)).title()
        print(description)


class NoNameHero(SuperHero):
    """ Class for secret hero"""

    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level, race, magiclevel)

    def show_hero(self):
        """" Print all parameters of this Hero """
        description = (": Level is:" + str(self.level) +
                       "; Race is:" + self.race +
                       "; Health is:" + str(self.health) +
                       # "; Magic is:" + str(self.magic) +
                       "; Magic level is:" + str(self.magiclevel)).title()
        print(description)

