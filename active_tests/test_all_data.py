import sys
from aws_costs_api.SQLiteRepository import SQLiteRepository

try:
    connectionString = sys.argv[1]
except IndexError:
    print("Yoy must put the first argument as a connection string for the database.")
    exit()
    
sqliteRepository = SQLiteRepository()
sqliteRepository.setConnectionString(connectionString)
print(sqliteRepository.all())