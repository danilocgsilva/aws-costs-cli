from aws_costs_api.AWSCosts import AWSCosts
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_cli.CSV import CSV
from aws_costs_cli.OutOfOptionException import OutOfOptionException

def main():

    dcgsPHelpers = DcgsPythonHelpers()
    args = dcgsPHelpers.command_line_argument_names(
        'profile', 'p', 'types', 't', 'format', 'f', 'start-time', 'st', 'currency', 'c'
    )
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)

    if args.start_time:
        awscosts.setStartTime(args.start_time)

    if args.types:
        for service in args.types.split(","):
            awscosts.setService(getServiceTranslation(service))

    if args.format:
        csvString = CSV().setAWSCostsClass(awscosts).get()
        print(csvString)
    else:
        TerminalFormatter().get(awscosts.getCosts())


def getServiceTranslation(shortServiceName: str) -> str:

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

    if shortServiceName in serviceTranslationBag:
        return serviceTranslationBag[shortServiceName]
    else:
        message = "Option not known. Acceptable values are:\n"
        for key in serviceTranslationBag:
            message += key + "\n"
        raise OutOfOptionException(message)
