# cars = ["rolls royce", "mercedeces benz", "bugatti", "porshce"]

# def add_car(s: str, l: list):
#     l.append(s)
#     return l

# add_car("lamboghini", cars)
# print(cars)

# def remove_cars(key, l: list):
#     if type(key) is int and key < len(l) and key >= len(l)*-1:
#         l.pop(key)
#     if type(key) is str:
#         l.remove(key)
#         return l

# remove_cars(1, cars)
# print(cars)

# def insert_cars(key, s: str, l: list):
#     if type(key) is int:
#         l.insert(key, s)
#         return l

# insert_cars(3, "camry", cars)
# print(cars)

# def display_cars(l: list):
#     print(l)
#     return
# display_cars(cars) 

squad_memb = ["mbappe", "bellingham", "vini jr", "lamine yamal"]

def add_footballer(l: list):
    name = input("Player name: ")
    if name == "":
        print("the footballer name cannot be empty")
    l.append(name)
    print("Footballer added successfully")
       
def remove_footballer(l: list):
    name = input("Enter the footballer's name you want to remove: ")
    if name == "":
        print("\nThe name cannot be empty")
    
    elif name in l:
        l.remove(name)
        print("\nThe footballer was removed successfully")
    else:
        print(f"\nPlayer '{name}' was not found in the list.\nReturning to menue . . .\n")

def show_footballer(l: list):
    print("---\nCurrent Ballers\n---")
    for players in l:
        print(f"*-{players}")
    print()


def count_footballers(l: list):
        print("The numbers of footballers is : {len(l)}\n")
        

def exit_football(l: list):
    # for players in l:
        print("exited successfully")
        exit()

def footballer_menu(l: list):

    while True:
        
        print("-----------------------------\n FOOTBALLER MANAGER MENU \n-----------------------------")
        print("1. Add a player")
        print("2. Remove a player")
        print("3. Show all the player")
        print("4. Count the players")
        print("5. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            add_footballer(l)

        elif choice == "2":
            remove_footballer(l)
    
        elif choice == "3":
            show_footballer(l)

        elif choice == "4":
            count_footballers(l)

        elif choice == "5":
            exit_football(l)

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    footballer_menu(squad_memb)

