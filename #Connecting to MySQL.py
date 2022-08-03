#Connecting to MySQL
from __future__ import print_function
import mysql.connector
import mysql.connector
import os
  
# Get the value of 'HOME'
# environment variable
key = 'DB_USER'
user = os.getenv(key)

# Print the value of 'HOME'
# environment variable
  
# Get the value of 'JAVA_HOME'
# environment variable
key = 'DB_PASSWORD'
password = os.getenv(key)
  
# Print the value of 'JAVA_HOME'
# environment variable

# read environment variable DB_USER for user and DB_PASSWORD for password to use to connect to


cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='sample_game')


cursor = cnx.cursor()

add_player = ("INSERT INTO player "
               "(first_name, last_name, address, recentScore) "
               "VALUES (%s, %s, %s, %s)")
data_player = ('Khurram', 'Nieeeeezami', '2240 swift blvd', '9708')


# Insert new employee
cursor.execute(add_player, data_player)


add_item = ("INSERT INTO item "
              "(name, uses, description, cost, player_id) "
              "VALUES (%s, %s, %s, %s, %s)")

# Insert salary information
data_item = ('Mera Mera noeeeeeee Mi', 99, 'Re: Legend of Ace', 10, 4)





cursor.execute(add_item, data_item)

print('finished')
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()