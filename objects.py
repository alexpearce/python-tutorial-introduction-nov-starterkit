class Person(object):
    species = 'Human'
    def __init__(self, name, age=32):
        self.name = name
        self.age = 42

    def describe(self):
        print self.name
        print self.age

    def introduce(self):
        return 'I am {0} and I am {1} years old'.format(
            self.name,
            self.age
        )

alice = Person('Alice')
bob = Person('Bob')
alice.introduce()
bob.introduce()
