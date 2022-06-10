from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_cli.CSV import CSV
from aws_costs_cli.functions import spread, getServiceTranslation
import argparse

def main():
    args = __get_arguments_parsed()
    
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)

    if args.start_time:
        awscosts.setStartTime(args.start_time)

    if args.types:
        for service in args.types.split(","):
            awscosts.setService(getServiceTranslation(service))

    terminal_formatter = TerminalFormatter()

    if not args.spread_services:
        if args.format:
            csvString = CSV().setAWSCostsClass(awscosts).get()
            print(csvString)
        else:
            terminal_formatter.get(awscosts.getCosts())
    else:
        data_all_services = spread(awscosts)
        terminal_formatter.set_all_data_services(data_all_services)
        terminal_formatter.print_spread()
            

def __get_arguments_parsed():
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profile",
        "-",
        help="The profile with the cost visualization enabled."
    )
    parser.add_argument(
        "--types",
        "-t",
        help="Types of costs in filter. Ex.: workmail,sns"
    )
    parser.add_argument(
        "--format",
        "-f",
        help="If you want to print in csv. Ex.: --format csv"
    )
    parser.add_argument(
        "--start-time",
        "-st",
        help="If you want to change the default starting time to considers the cost (default 1 month). Ex.: --start-time 2022-02-16"
    )
    parser.add_argument(
        "--spread-services",
        "-ss",
        action="store_true",
        help="Shows the cost for each service."
    )
    
    return parser.parse_args()


