class Perpon(object):
    def __init__(self, name):
        print("Perpon run")
        self.__name = name

    @property
    def name(self):
        return self.__name


class Father(Perpon):
    def __init__(self, name, age, job):
        print("Father run")
        super(Father, self).__init__(name, job)
        self.__age = age

    @property
    def age(self):
        return self.__age


class Mother(Perpon):
    def __init__(self, name, job):
        print("Mother run")
        super().__init__(name)
        self.__job = job

    @property
    def job(self):
        return self.__job


class Son(Father, Mother):
    def __init__(self, genter, name, age, job):
        super(Son, self).__init__(name, age, job)
        print("Son run")
        self.__genter = genter

    @property
    def genter(self):
        return self.__genter


tom = Son("汤姆", 21, "Boy", "Teacher")
print(tom.name)
print(tom.age)
print(tom.genter)
print(tom.job)