import os
from aws_costs_api.Storage.SQLiteRepository import SQLiteRepository
from aws_costs_api.Storage.MysqlRepository import MysqlRepository
from aws_costs_api.MongoRepository import MongoRepository
import json

def main():
    connectionStringParts = os.environ.get("CONNECTIONSTRING").split(":")
    connectionStringType = connectionStringParts[0]
    connectionString = connectionStringParts[1]

    if connectionStringType == "sqlite":
        repository = SQLiteRepository()
    elif connectionStringType == "mysql":
        repository =  MysqlRepository()
    repository.setConnectionString(connectionString)
    
    mongoRepository = MongoRepository()
    
    for entry in repository.allGenerator():
        valueDicted = json.loads(entry["value"])
        print(type(valueDicted).__name__)
        mongoRepository.store(entry["key"], valueDicted)
