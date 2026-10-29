from pet import *
print("Welcome to the virtual pet simulator!")
has_pet = input("Do you already have a pet? Y/N")
def create_pet():
    name = input("Give a name for your pet: ")
    print("Configuring your virtual pet friend...")
    pet = init_pet(name)
    print(f"Your pet {pet.name} is configured!")
    print(f"Your pet will start with {pet.health} hp and {pet.happiness} happiness points")


if has_pet.lower() == "n" or "no":
    create_pet()
