
class Car:

    def __init__(self, make, model, price, year_of_production, color):
        self.make = make
        self.model = model
        self.price = price
        self.year_of_production =year_of_production
        self.color = color

    def drive(self):
        print(self.make, self.model, "is driving")

    def info(self):
        return f'Make: {self.make}, Model: {self.model}, Price: {self.price},' \
               f' Year: {self.year_of_production}, Color: {self.color}'


car = Car('BMW', 'i8000', 12000000, 2018, 'Black')
# print(car.info())
# car.drive()

audiA8 = Car('Audi', 'A8', 10000000, 2020, 'Red')
#print(audiA8.info())

car2 = Car('Mersedes-Benz', 'S-Class', 21300000, 2021, 'Gray')
car3 = Car('Toyota', 'Rav4', 21300000, 2021, 'Brown')
car4 = Car('Honda', 'CRV', 250000, 2021, 'Yellow')
car7 = Car('Honda', 'CRV', 250000, 2020, 'Yellow')
car5 = Car('Toyota', 'Heilander', 250000, 2019, 'Yellow')
car6 = Car('Toyota', 'Camry', 250000, 2020, 'Yellow')


list_of_cars =(car, audiA8, car2, car3, car4, car5, car6, car7)
for i in list_of_cars:
    print(i.info())

for i in list_of_cars:
    if i.year_of_production == 2018:
        i.drive()
    if i.year_of_production == 2018 or i.year_of_production == 2020:
        print(i.year_of_production, i.price)
    if i.year_of_production == 2021:
        print(i.model)


dictionary = {car.make: [car, ]}

for i in list_of_cars:
    if i.make in dictionary.keys():
        dictionary[i.make].append(i)
    else:
        dictionary.setdefault(i.make, i)

print(dictionary)