import os
from aws_costs_api.SQLiteRepository import SQLiteRepository
from aws_costs_api.MongoRepository import MongoRepository
import json

def main():
    connectionString = os.environ.get("SQLITECONNECTIONSTRING")
    sqliteRepository = SQLiteRepository()
    sqliteRepository.setConnectionString(connectionString)
    
    mongoRepository = MongoRepository()
    
    for entry in sqliteRepository.allGenerator():
        valueDicted = json.loads(entry["value"])
        print(type(valueDicted).__name__)
        mongoRepository.store(entry["key"], valueDicted)
