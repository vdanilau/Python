from hero import Hero

#------------ Main ---------------

myhero1 = Hero("Werfolf", 5, "animal")
myhero2: Hero = Hero("Alexander", 4, "Human")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()

