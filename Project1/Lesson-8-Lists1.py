cities = ['New York', 'Moscow', 'new dehli', 'Minsk', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[-1]) #С конца массива распечатать первый
print(cities[2].title())
print(cities[2].upper())
print(cities[0].lower())

cities[1] = 'Tula'
print(cities)

cities.append('Kursk')
print(cities)

cities.append("Mumbai")
print(cities)

cities.insert(1, 'Paris')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop(1)
print("Deleted city is " + deleted_city)
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)