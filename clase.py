import random
 
 
#games are all the titles of games that the program can use; participants can give their own propositions
games = ["Pokemon(1)", "Fortnite(2)", "Minecraft(3)", "CS(4)"]
#list_of_games_to_guess is the variable into which we insert the password to guess
list_of_games_to_guess = []
#list_of_entered_games is a list of games entered by the user
list_of_entered_games = []
###EVERYTHING ABOVE IS A STARTER PROJECT
 
number_of_attemps = 0

for i in range(4):
    game_drawn = random.choice(games)
    list_of_games_to_guess.append(game_drawn)

 
###STARTER
#we display the instructions 
print("Welcome to the MasterMind game")
print("Your goal is to guess the 4 games that have been drawn by the computer as quickly as possible.")
print("The order of the games is relevant when guessing.")
print("Please note the games may be duplicated!!!")
print("Here is the set of games used by the computer")
print(games)
# int = NUMEROS ENTEROS
# != ES DECIR DIFERENTE
# while significa mientras que 

while list_of_games_to_guess != list_of_entered_games:
    list_of_entered_games = []
    print("nuevo intento")
    print(games)

    for i in range(4):
        game_entered = int(input(f"ingresa el juego numero {i+1}"))
        game = games[game_entered - 1]
        list_of_entered_games.append(game)


guessed_games = 0

for i in range(4):
    if list_of_entered_games[i] == list_of_games_to_guess[i]:
        print(f"{i+1} - {list_of_entered_games[i]} - correcto")
        guessed_games = guessed_games + 1 
    else :
        print(f" {i+1} - {list_of_entered_games[i]} - incorrecto")

    number_of_attemps+=1
    print(f"number of attempts:{number_of_attemps}")
    


'''lista = ["Saul", "Daniel" , "Alex", "Adria"]
lista[3]'''

