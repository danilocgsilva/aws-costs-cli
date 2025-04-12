from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.SpreadCalculator import SpreadCalculator
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_cli.CSV import CSV
from aws_costs_cli.functions import getServiceTranslation, serviceTranslationBag
import argparse
import json
import os
from aws_costs_cli.functions import result_spread_services

def main():
    args = __get_arguments_parsed()
    
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)

    if args.start_time:
        awscosts.setStartTime(args.start_time)

    if args.types:
        for service in args.types.split(","):
            awscosts.setService(getServiceTranslation(service))
            
    connectionString = os.environ.get("CONNECTIONSTRING")
        
    terminal_formatter = TerminalFormatter()

    if not args.spread_services:
        if args.format:
            if args.format == "csv":
                csvString = CSV().setAWSCostsClass(awscosts).get()
                print(csvString)
            elif args.format == "awsraw":
                print(
                    json.dumps(
                        awscosts.getCosts(connectionString),
                        indent=4
                    )
                )
            else:
                raise Exception("This format is not implemented yiet!")
        else:
            terminal_formatter.get(awscosts.getCosts(connectionString))
    else:
        if args.format == "csv":
            csv = CSV()
            csv.setAWSCostsClass(awscosts)
            csv.setSpread(serviceTranslationBag)
            results = csv.get()
            print(results)
        else:
            spreadCalculator = SpreadCalculator()
            spreadCalculator.set_client(awscosts)
            spreadCalculator.set_translation_bag(serviceTranslationBag)
            result_spread_services(spreadCalculator, terminal_formatter, connectionString)

def __get_arguments_parsed():
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profile",
        "-p",
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
        help="If you want to print in csv. Ex.: --format csv. Availables: csv, awsraw"
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

