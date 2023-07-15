import sys
sys.path.append("../..")
from aws_costs_api.MongoRepository import MongoRepository

try:
    key = sys.argv[1]
    mongoRepository = MongoRepository()
    dataExists = mongoRepository.dataExists(key)
    if dataExists:
        print("The provided key exists in database.")
    else:
        print("The provided key does not exists in database.")
except IndexError:
    print("It is required to provides a value in the first argument in command line to tell the name of key to search for.")
