from pet import *
import pandas
import csv
import random
print("Welcome to the virtual pet simulator!")
has_pet = input("Do you already have a pet? Y/N")

pet = Pet

def save_pet_data(pet):
    print("Saving pet data...")
    out_data = {
        "name": [pet.name],
        "health": [pet.health],
        "happiness": [pet.happiness]
    }
    df = pandas.DataFrame(out_data)
    df.to_csv("pet_data.csv")
def create_pet():
    global pet
    name = input("Give a name for your pet: ")
    print("Configuring your virtual pet friend...")
    pet = init_pet(name)
    save_pet_data(pet)
    print(f"Your pet '{pet.name}' is configured!")
def load_pet():
    global pet
    with open("pet_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        pet_data = next(reader)
    pet = Pet(pet_data["name"], int(pet_data["health"]), int(pet_data["happiness"]))
    return pet

def simulator(name, hp, happiness):
    pet_obj = Pet(name, hp, happiness)
    print(f"{name}: Hi!")
    age = 1
    is_dead = False
    while is_dead == False:
        if age >= random.randint(1024, 65536) or hp <= 0:
            print("Your pet died")
            is_dead = True
            break
        if age % 5 == 0:
            print("Saving pet data...")
            save_pet_data(pet_obj)
        print(f"Day {age}")
        print("You must feed your pet and play with it")
        feed = input("Do you want to feed it? Enter 'feed'")
        entertain = input("Do you want to play with it? Enter 'play'")
        if feed.lower() != "feed":
            hp = hp - random.randint(1, 6)
            print("Please feed your pet next time!")
        if entertain.lower() != "play":
            happiness = happiness - random.randint(1, 6)
        if happiness <= 0:
            hp = hp - 1
            print("Please entertain your pet!")
        print(f"{name}'s stats today: {hp} health, {happiness} happiness")
        cont = input("Continue to the next day? Type 'exit' to exit simulator")
        if cont.lower() == 'exit':
            save_pet_data(pet_obj)
            break
        age = age + 1

if has_pet.lower() == "n" or has_pet.lower() == "no":
    create_pet()
elif has_pet.lower() == "y" or has_pet.lower() == "yes":
    load_pet()

print(f"Your pet '{pet.name}' has {pet.health} hp and {pet.happiness} happiness points")
ready = input("Are you ready to start the simulator? ")
if ready.lower() == "y" or ready.lower() == "yes":
    simulator(pet.name, pet.health, pet.happiness)
