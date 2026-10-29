def simulator(name, hp, happiness):
    age = 1
    is_dead = False
    while is_dead == False:
        if age >= 3:
            print("Your pet died")
            is_dead = True
            break
        print(f"Day {age}")
        print(f"{name}'s stats today: {hp} health, {happiness} happiness")
        input("Continue?")
        age = age + 1
