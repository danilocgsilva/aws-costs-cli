from aws_costs_api.AWSCosts import AWSCosts

def main():
    awscosts = AWSCosts()
    results = awscosts.getCosts()
    print(results)

