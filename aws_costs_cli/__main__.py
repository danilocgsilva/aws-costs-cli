from aws_costs_api.AWSCosts import AWSCosts
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

def main():
    
    dcgsPHelpers = DcgsPythonHelpers()
    args = dcgsPHelpers.command_line_argument_names('profile', 'p')
    
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)
    results = awscosts.getCosts()
    print(results)
