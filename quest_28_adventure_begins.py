def forest():
    print("\nYou enter a dark forest. The air smells damp and ancient.")
    choice = input("Do you follow the sound of water or climb a tree? (water/tree): ").lower()

    if choice == "water":
        river()
    elif choice == "tree":
        print("\nYou climb the tree and spot a village in the distance.")
        print("You safely find your way home. Ending: The Wise Explorer.")
    else:
        print("\nConfused, you wander until night falls. Ending: Lost in the Woods.")


def river():
    print("\nYou approach a rushing river.")
    choice = input("Do you swim across or build a raft? (swim/raft): ").lower()

    if choice == "swim":
        print("\nThe current is too strong.")
        print("Ending: Swept Away.")
    elif choice == "raft":
        print("\nYour raft holds steady.")
        print("You discover hidden treasure on the other side!")
        print("Ending: The River Conqueror.")
    else:
        print("\nYou hesitate too long. Night creatures stir.")
        print("Ending: Frozen by Fear.")


def start():
    print("Welcome to the Adventure.")
    print("You stand at the edge of a mysterious forest.")
    choice = input("Do you enter or walk away? (enter/leave): ").lower()

    if choice == "enter":
        forest()
    elif choice == "leave":
        print("\nYou choose safety over danger.")
        print("Ending: The Cautious Survivor.")
    else:
        print("\nUnable to decide, time passes you by.")
        print("Ending: The Indecisive Wanderer.")


start()