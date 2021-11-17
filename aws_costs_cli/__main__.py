from aws_costs_api.AWSCosts import AWSCosts
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from aws_costs_cli.FormatSingle import FormatSingle
from aws_costs_cli.OutOfOptionException import OutOfOptionException

def main():

    dcgsPHelpers = DcgsPythonHelpers()
    args = dcgsPHelpers.command_line_argument_names('profile', 'p', 'types', 't')
    awscosts = AWSCosts()
    awscosts.setProfile(args.profile)

    if args.types:
        for service in args.types.split(","):
            awscosts.setService(getServiceTranslation(service))

    results = awscosts.getCosts()

    amount = 0

    for result in results["ResultsByTime"]:
        formatSingle = FormatSingle(result)
        amount += formatSingle.getAmount()
        __showData(formatSingle)

    __finishes(str(amount), formatSingle.getAmountUnit())

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


def __finishes(amount, unit):
    print("Total from last month: " + amount + " " + unit)
    print("---//---")
    print("Above, the last month day by day cost from AWS account.")

def __showData(format: FormatSingle):
    print(
        "Month and day: " + format.getMonthDay()
    )
    print(
        str(format.getAmount()) + " " + format.getAmountUnit()
    )
    print("----")

