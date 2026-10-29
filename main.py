from pet import *
from simulator import *
import pandas
import csv
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
    pet = Pet(pet_data["name"], pet_data["health"], pet_data["happiness"])
    return pet

if has_pet.lower() == "n" or has_pet.lower() == "no":
    create_pet()
elif has_pet.lower() == "y" or has_pet.lower() == "yes":
    load_pet()

print(f"Your pet '{pet.name}' has {pet.health} hp and {pet.happiness} happiness points")
ready = input("Are you ready to start the simulator? ")
if ready.lower() == "y" or ready.lower() == "yes":
    simulator(pet.name, pet.health, pet.happiness)
