import os
from aws_costs_api.Repository import Repository

def main():
    print("Lets translate the database to mongo.")
    connectionString = os.environ.get("SQLITECONNECTIONSTRING")
    