from aws_costs_cli.OutOfOptionException import OutOfOptionException

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

def getServiceTranslation(shortServiceName: str) -> str:

    if shortServiceName in serviceTranslationBag:
        return serviceTranslationBag[shortServiceName]
    else:
        message = "Option not known. Acceptable values are:\n"
        for key in serviceTranslationBag:
            message += key + "\n"
        raise OutOfOptionException(message)


