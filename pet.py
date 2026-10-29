class Pet:
    def __init__(self, name, health=20, happiness=20):
        self.name = name
        self.health = health
        self.happiness = happiness

def init_pet(name):
    pet = Pet(name)
    return pet
