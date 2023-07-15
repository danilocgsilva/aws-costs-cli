import sys
sys.path.append("../..")
from aws_costs_api.MongoRepository import MongoRepository

mongoRepository = MongoRepository()

try:
    key = sys.argv[1]
    value = sys.argv[2]

    mongoRepository.store(key, value)
except IndexError:
    print("Its is required a second and a third argument in the commandline as well to perform the testes.")


