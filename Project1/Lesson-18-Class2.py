from hero import Hero, SuperHero, NoNameHero

myhero = Hero("Maksimus", 4, "ork")
mysuperhero = SuperHero("Moisey", 10, "human", 5)
mynonamehero = NoNameHero("Jora", 15, "shadow", 16)


myhero.show_hero()
mysuperhero.magic = 10 # так нельзя делать, но тут и не сработает из за __magic в описании классов
mysuperhero.show_hero()
mysuperhero.make_magik()
mysuperhero.make_magik()
mysuperhero.make_magik()
mysuperhero.magiclevel = 10 # а тут сработает, т.к. нет защиты
mysuperhero.show_hero()
mynonamehero.show_hero()