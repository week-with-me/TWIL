class Dog:
    def bark(self):
        print("I'm a dog.")


class Husky(Dog):
    def bark(self):
        print("I'm a Husky.")
        
        
class Corgi(Dog):
    def bark(self):
        print("I'm a Corgi.")     


# Husky First

class Horgi(Husky, Corgi):
    pass

print("MRO: ", Horgi.mro())
horgi = Horgi()
horgi.bark()


# Corgi First

class Horgi(Corgi, Husky):
    pass

print("MRO: ", Horgi.mro())
horgi = Horgi()
horgi.bark()


# Super

class Husky(Dog):
    def bark(self):
        return super().bark()
    
class Horgi(Husky, Corgi):
    pass

print("MRO: ", Horgi.mro())
horgi = Horgi()
horgi.bark()


# TypeError

class Horgi(Dog, Husky, Corgi):
    pass


class Horgi(Husky, Corgi, Dog):
    pass

print("MRO: ", Horgi.mro())
horgi = Horgi()
horgi.bark()