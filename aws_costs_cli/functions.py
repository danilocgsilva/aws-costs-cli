from aws_costs_cli.OutOfOptionException import OutOfOptionException
from aws_costs_api.AWSCosts import AWSCosts

serviceTranslationBag = {
    "tax": "Tax",
    "ec2": "EC2 - Other",
    "compute": "Amazon Elastic Compute Cloud - Compute",
    "s3": "Amazon Simple Storage Service",
    "workmail": "AmazonWorkMail",
    "cloudwatch": "AmazonCloudWatch",
    "sns": "Amazon Simple Notification Service",
    "route53": "Amazon Route 53",
    "rds": "Amazon Relational Database Service",
    "codecommit": "AWS CodeCommit",
    "dynamodb": "Amazon DynamoDB",
    "kms": "AWS Key Management Service",
    "cloudfront": "Amazon CloudFront",
    "efs": "Amazon Elastic File System",
    "ce": "AWS Cost Explorer"
}

def spread(awscosts: AWSCosts) -> dict:

    by_date_service_data = {}
    for key_service in serviceTranslationBag:
        awscosts.setUniqueService(getServiceTranslation(key_service))
        results_by_time = awscosts.getCosts()["ResultsByTime"]
        for single_result in results_by_time:
            single_result = __shrink_data(single_result, key_service)

            if not single_result["period"] in by_date_service_data:
                by_date_service_data[single_result["period"]] = {}

            by_date_service_data[single_result["period"]][key_service] = single_result["amount"]

    for date in by_date_service_data:
        date_sum = 0
        for service_key in by_date_service_data[date]:
            date_sum += by_date_service_data[date][service_key]
        by_date_service_data[date]["TOTAL"] = date_sum

    return by_date_service_data

def getServiceTranslation(shortServiceName: str) -> str:

    if shortServiceName in serviceTranslationBag:
        return serviceTranslationBag[shortServiceName]
    else:
        message = "Option not known. Acceptable values are:\n"
        for key in serviceTranslationBag:
            message += key + "\n"
        raise OutOfOptionException(message)

def __shrink_data(raw: dict, key_service: str) -> dict:

    return {
        "service": key_service,
        "period": raw["TimePeriod"]["Start"],
        "amount": float(raw["Total"]["BlendedCost"]["Amount"]),
        "unit": raw["Total"]["BlendedCost"]["Unit"]
    }

