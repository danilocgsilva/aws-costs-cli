from aws_costs_api.AWSCosts import AWSCosts
from numpy import result_type
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_cli.CSV import CSV
from aws_costs_cli.OutOfOptionException import OutOfOptionException
import argparse

serviceTranslationBag = {
    "ec2": "EC2 - Other",
    "s3": "Amazon Simple Storage Service",
    "workmail": "AmazonWorkMail",
    "tax": "Tax",
    "cloudwatch": "AmazonCloudWatch",
    "sns": "Amazon Simple Notification Service",
    "route53": "Amazon Route 53",
    "rds": "Amazon Relational Database Service",
    "codecommit": "AWS CodeCommit",
    "dynamodb": "Amazon DynamoDB"
}

def main():
    args = __get_arguments_parsed()
    
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)

    if args.start_time:
        awscosts.setStartTime(args.start_time)

    if args.types:
        for service in args.types.split(","):
            awscosts.setService(getServiceTranslation(service))

    if not args.spread_services:
        if args.format:
            csvString = CSV().setAWSCostsClass(awscosts).get()
            print(csvString)
        else:
            TerminalFormatter().get(awscosts.getCosts())
    else:
        for key_service in serviceTranslationBag:
            awscosts.setUniqueService(getServiceTranslation(key_service))
            results_by_time = awscosts.getCosts()["ResultsByTime"]
            for single_result in results_by_time:
                single_result["service"] = key_service
                single_result["period"] = single_result["TimePeriod"]["Start"]
                single_result.pop("TimePeriod", None)
                single_result.pop("Estimated", None)
                single_result.pop("Groups", None)
                single_result["amount"] = single_result["Total"]["BlendedCost"]["Amount"]
                single_result.pop("Total", None)
                print(single_result)

def getServiceTranslation(shortServiceName: str) -> str:

    if shortServiceName in serviceTranslationBag:
        return serviceTranslationBag[shortServiceName]
    else:
        message = "Option not known. Acceptable values are:\n"
        for key in serviceTranslationBag:
            message += key + "\n"
        raise OutOfOptionException(message)

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

def __extract_single_result(raw: dict) -> dict:
    time = raw["TimePeriod"]["Start"]
    service = raw["Service"]
    amount = raw["Total"]["BlendedCost"]["Amount"]

    return {
        "time": time,
        "service": service,
        "amount": amount
    }