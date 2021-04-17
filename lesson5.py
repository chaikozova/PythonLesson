paitans = {12.04: 89, 13.04: 120, 14.04: 50, 15.05: 34}


class Person():
    def __init__(self, name, surname, age, sex, status):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.status = status


girl = Person("Alex", "Brown", 13, 'women', 'not married')
print(girl.name, girl.surname, girl.age, girl.sex, girl.status)