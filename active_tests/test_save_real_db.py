import sys
from aws_costs_api.SQLiteRepository import SQLiteRepository

try:
    connectionString = sys.argv[1]
except IndexError:
    print("Yoy must put the first argument as a connection string for the database.")
    exit()

try:
    keyStored = sys.argv[2]
except IndexError:
    print("Yoy must put a second argument to be the key to be stored.")
    exit()

try:
    valueStored = sys.argv[3]
except IndexError:
    print("Yoy must put a third argument to be value to be stored.")
    exit()

sqliteRepository = SQLiteRepository()

print("Your connection string is: " + connectionString)
sqliteRepository.setConnectionString(connectionString)
sqliteRepository.store(keyStored, valueStored)
