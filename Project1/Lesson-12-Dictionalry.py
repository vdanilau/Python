enemy = {
            'loc_x': 70,
            'loc_y' : 50,
            'color' : 'green',
            'health': 100,
            'name'  : 'Mudillo',
            'image': ['image1.jpg', 'image1.jpg', 'image3.jpg']
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

for en in all_enemies:
    print(en)

print("-----------END-----------\n")

all_enemies[5]['health'] = 30
all_enemies[8]['name'] = 'Kozel'
all_enemies[2]['loc_x'] += 10

for en in all_enemies:
    print(en)