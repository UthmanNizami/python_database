from __future__ import print_function
from email import message
import json
import mysql.connector
import mysql.connector
import os

key = 'DB_USER'
user = os.getenv(key)

# Print the value of 'HOME'
# environment variable
  
# Get the value of 'JAVA_HOME'
# environment variable
key = 'DB_PASSWORD'
password = os.getenv(key)

cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='sample_game')
cursor = cnx.cursor()

# show_players receives a list of players into variable named "players"  It then goes through the players and displays them.
#
# 1.  open a file called "players.dat".  If the file already exists, append to the file.  If it doesn't, it should create a new file.  
#     You should write the players first name, last name, and recent score to the file.
#
# TODO:  Encrypt player data before saving it to a file
from cryptography.fernet import Fernet

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()


def save_players():
    for player in PlayerList:
        add_player = ("INSERT INTO player "
               "(first_name, last_name, address, recentScore) "
               "VALUES (%(first)s, %(last)s, %(address)s, %(recentScore)s)")
        data_player = player
    cursor.execute(add_player, data_player)
    cnx.commit()


def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(message):
    key = load_key()
    f = Fernet(key)
    message = f.decrypt(message)
    decoded_message = message.decode()

    print(decoded_message)
    return decoded_message

def show_players():
    query = ("SELECT first_name, last_name, recentScore, address FROM player ")

    cursor.execute(query)

    for (first, last, recentScore, address) in cursor:
        print("{} {} has a recent score of {} and lives at {}".format(
        first, last, recentScore, address))


def read_and_load_players():
    #print("The player list is: {}".format(PlayerList))
    still_reading = True
    f = open("players.dat", "rb")
    players = f.read()
    decrypted_players = decrypt_message(players)
    print("players is {}".format(decrypted_players))
    PlayerList = json.loads(decrypted_players)
    f.close()

    # expected output ""Contents of PlayerData: { "first": <first name>, "last": <last name>, "score": <entered score>}"
    return

PlayerList = []
# Ask the user if they want to create new players or if they want to laod the existing saved players.
# If the user wants to add new players then go ahead and ask for new players as usual.
# If the user wants to load existing players then run the function read_and_load_players()
load = False
print("Do you want to load the existing players or add new players?")
load = input("Enter 'existing' to load existing players or 'new' to create new players: ")
if load == "existing":
    read_and_load_players()
elif load == "new":
    add = False
    while add != "":
        PlayerData = {}
        add = input("Press enter to stop adding players. \nEnter the players first name: ")
        if add != "":
            PlayerData["first"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players last name: ")
        if add != "":
            PlayerData["last"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players recent score: ")
        if add != "":
            PlayerData["recentScore"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players address: ")
        if add != "":
            PlayerData["address"] = add
        PlayerList.append(PlayerData)
    save_players()

show_players()

cursor.close()
cnx.close()
