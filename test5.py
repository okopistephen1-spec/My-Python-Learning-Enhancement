# # # foods = {"akpu", "egusi", "japanese friedrice", "mango", "pando"}
# # # print(foods)

# # # clubs = ["real madrid", "barcelona", "psg", "athletico madrid", "liverpool"]

# # # bests = set(clubs)

# # # if "real madrid" in bests:
# # #     print("found")

# # #     print(bests)


# # batch_A = {"Ogenemingwo", "Otsefuefue", "Monday", "Somadina", "Osas"}

# # batch_B = {"Otsefuefue", "Monday", "Ogenemingwo", "Somadina", "Chukwuebuka"}

# # results = batch_A | batch_B

# # both = batch_A & batch_B

# # diff = batch_A - batch_B

# # symm_diff = batch_A ^ batch_B

# # print(results)
# # print(both)
# # print(diff)
# # print(symm_diff)


# # numbers = {1,2,2,2,2,4,4,3,5,6,7,7}

# # print(numbers)

# colors = {"red", "blue", "yellow", "purple", "green"}

# colors.add("orange")
# colors.discard("purple")

# if "blue" in colors:
#     print("Found Blue")

#     print(colors)


# scores = [4,5,5,6,7,7,8,8]

# goals = set(scores)

# print(goals)

# squad_player_A = {"Ronaldo", "Mbappe", "Messi", "Neymar"}

# squad_player_B = {"Pepe", "Rodrigo", "Mbappe", "Messi", "Neymar", "Ronaldo"}

# res1 = squad_player_A & squad_player_B
# res2 = squad_player_A | squad_player_B
# res3 = squad_player_A - squad_player_B
# print(res1)
# print(res2)
# print(res3)

def menu(l: set):
    while True:
        print("\n--------------------\nFootBall Reg. System\n--------------------\n")
        print("1. Register Player")
        print("2. Show All Players")
        print("3. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            regst_player(l)
        
        elif choice == 2:
            show_players(l)

        elif choice == 3:
            # break
            print("\nGoodbye. Thanks for trusting us")

        else:
            print("Invalid choice, Please choose a valid option")


def show_players(l: set):
    print("======All Players======")
    for player in l:
        print(player)



def regst_player(l: set):
    playr = input("Enter a player to register: ").strip().title()

    if playr in l:
        print("This already exist")
        return l

    l.add(playr)
    print("\nPlayer added successfully")
    return l

players = set()

menu(players)